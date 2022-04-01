import argparse
from concurrent.futures import process
import pickle
from enum import Enum

import numpy as np
import pygame
from pygame.locals import *


class NoneSound:
	    def play(self):
	        pass
	
	
def load_sound(fullname):
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    try:
        sound = pygame.mixer.Sound(fullname)
        #sound = pygame.mixer.music.load(fullname)
    except pygame.error as err:
        print("Cannot load sound: %s" % fullname)
        raise SystemExit(str(err))
    return sound


def load_image(fullname, trans=None, colorkey=None):
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise SystemExit(message)
    if trans is not None:
        for trans, params in trans.items():
            image = getattr(pygame.transform, trans)(image, *params)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class SceneManager():

    def __init__(self, initial_scene = 1, music = False):

        # escenas
        scenes = {}
        scenes[Scenes.MENU] = StartMenu()
        scenes[Scenes.GAME] = GameScene()
        scenes[Scenes.CREDITS] = Credits()
        self.scenes = scenes
        self.current_scene = scenes[Scenes(initial_scene)]
        self.current_scene.start()

        # musica
        self.music = music
        if self.music:
            self.sound = load_sound('game.wav')
            self.sound.play()

    def update(self, new_scene):
        if self.scenes[new_scene] is not self.current_scene:
            self.current_scene.stop()
            self.current_scene = self.scenes[new_scene]
            self.current_scene.start()

    def stop(self):
        if self.music:
            self.sound.stop()
class SceneBase:
    def __init__(self, bg_image=None):

        screen = pygame.display.get_surface()
        background = pygame.Surface(screen.get_size())
        background = background.convert()

        if bg_image:
            bg, rect = load_image(bg_image)
            background.blit(bg, rect)
        else:
            # fondo negro del mismo tamaño que la pantalla
            background.fill((0, 0, 0))

        self.background = background

    def start(self):
        pass

    def stop(self):
        pass

    def process_input(self, scene_manager):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
        return False

    def update(self, scene_manager):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.flip()


class Scenes(Enum):
    MENU = 1
    GAME = 2
    CREDITS = 3

class StartMenu(SceneBase):
    def __init__(self):
        super().__init__()

    
        start_btn, rect = load_image("start.png")
        credits_btn, credits_rect = load_image("credits.png")

        screen = pygame.display.get_surface()
        area = screen.get_rect()
        rect.center = area.center
        credits_rect.midbottom = area.midbottom
        self.background.blit(start_btn, rect)
        self.background.blit(credits_btn, credits_rect)

        self.game_rect = rect
        self.credits_rect = credits_rect

    def process_input(self, scene_manager):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                scene_manager.update(Scenes.GAME)
                return False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.game_rect.collidepoint(mouse_pos):
                    scene_manager.update(Scenes.GAME)
                    return False
                if self.credits_rect.collidepoint(mouse_pos):
                    scene_manager.update(Scenes.CREDITS)
                    return False
        return False

class Credits(SceneBase):
    def __init__(self):
        super().__init__()

        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render(
                "Tres en raya \n by Janus Noise", 1, (255, 255, 255))
            textpos = text.get_rect(
                centerx=self.background.get_width()/2,
                centery=self.background.get_height()/2
            )
            self.background.blit(text, textpos)


    def process_input(self, scene_manager):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                scene_manager.update(Scenes.MENU)
                return False
        return False




# class Agent():
#     def __init__(self):
#         self.value_function = pickle.load()
#         self.symbol = 1

#     def move(self, board):
#         valid_moves = board.valid_moves()
#         # vamos a la posición con más valor
#         max_value = -1000
#         for row, col in valid_moves:
#             next_board = board.state.copy()
#             next_board[row, col] = self.symbol
#             next_state = str(next_board.reshape(3*3))
#             value = 0 if self.value_function.get(next_state) is None else self.value_function.get(next_state)
#             if value >= max_value:
#                 max_value = value
#                 best_row, best_col = row, col
#         return best_row, best_col



class Board():
    def __init__(self):
        self.state = np.zeros((3,3))

    def valid_moves(self):
        return [(i, j) for j in range(3) for i in range(3) if self.state[i, j] == 0]

    def update(self, symbol, row, col):
        if self.state[row, col] == 0:
            self.state[row, col] = symbol
        else:
            raise ValueError("movimiento invalido !")

    def is_game_over(self):
        # comprobar filas y columnas
        if (self.state.sum(axis=0) == 3).sum() >= 1 or (self.state.sum(axis=1) == 3).sum() >= 1:
            return 1
        if (self.state.sum(axis=0) == -3).sum() >= 1 or (self.state.sum(axis=1) == -3).sum() >= 1:
            return -1 
        # comprobar diagonales
        diag_sums = [
            sum([self.state[i, i] for i in range(3)]),
            sum([self.state[i, 3 - i - 1] for i in range(3)]),
        ]
        if diag_sums[0] == 3 or diag_sums[1] == 3:
            return 1
        if diag_sums[0] == -3 or diag_sums[1] == -3:
            return -1        
        # empate
        if len(self.valid_moves()) == 0:
            return 0
        # seguir jugando
        return None

    def reset(self):
        self.state = np.zeros((3,3))

class Player():
    def __init__(self, color):
        self.turno = 9
        self.player_1_symbol = -1
        self.player_2_symbol = 1
        self.color = color



class GameScene(SceneBase):
    def __init__(self):
        super().__init__()
        self._game_over = False

        # cuadrícula
        screen = pygame.display.get_surface()
        size = screen.get_size()
        rect_width, rect_height = 5, 5
        for i in range(2):
            rect = pygame.Rect(
                (i+1)*(size[0] / 3) - 0.5*rect_width, 0, rect_width, size[1])
            pygame.draw.rect(self.background, (255, 255, 255), rect)
            rect = pygame.Rect(
                0, (i+1)*(size[1] / 3) - 0.5*rect_height, size[0], rect_height)
            pygame.draw.rect(self.background, (255, 255, 255), rect)
        
        self.initial_background = self.background
        self.background = self.initial_background.copy()
        self.size = size

        # objects
        self.players = [Player(i) for i in range(2)]
        #self.agent = Agent()
        self.board = Board()


    def start(self):
        self._game_over = False
        self.board.reset()
        self.background = self.initial_background.copy()

    def grid2pixels(self, x, y):
        x = (x*2 + 1)*(self.size[0]/6)
        y = (y*2 + 1)*(self.size[1]/6)
        return x, y

    def process_input(self, scene_manager):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
            # cambiar escena
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:                
                scene_manager.update(Scenes.MENU)
                return False
            # click en la cuadrícula
            elif event.type == pygame.MOUSEBUTTONDOWN and not self._game_over:
                # coordenadas del click
                x = int(event.pos[0] // (self.size[0] / 3))
                y = int(event.pos[1] // (self.size[1] / 3))
                # movimiento jugador
                if (y, x) in self.board.valid_moves():
                    self.board.update(self.player.player_1_symbol, y, x)
                    self.update_board(x, y)
                    # comprobar si jugador 1 ha ganado o hay empate
                    if self.board.is_game_over() == self.player.player_1_symbol:
                        self.game_over("You Win !")
                        break
                    if self.board.is_game_over() == 0:
                        self.game_over("It's a draw")
                        break
                    self.turno -= 1
                    # mueve el agente
                    #time.sleep(random.random() + 1.)
                    #y, x = self.agent.move(self.board)
                    #self.board.update(self.agent.symbol, y, x)
                    #self.update_board(x, y)
                    #if self.board.is_game_over() == self.agent.symbol:
                    #    self.game_over("Game Over :(")
                return False
        return False
    
    def turno(): 
            # Se mantiene alerta hasta que alguien gana
        hecho = False
        while not hecho:
            # Iteramos para cada jugador
            for jugador in self.players:
                # Procesamos sus turnos
                hecho = process_input()
                # Si alguien gana, 'rompemos' el bucle y finalizamos el juego.
                if hecho:
                    break
    
    def procesa_turno(): 


    def update_board(self, j, i):
        # pintar marcadores
        x, y = self.grid2pixels(j, i)
        state = self.board.state[i, j]
        if state == -1:
            width, height = 50, 50
            rect = pygame.Rect(
                x - width / 2, y - height / 2, width, height)
            pygame.draw.rect(
                self.background, (255, 255, 255), rect)
        elif state == 1:
            pygame.draw.circle(self.background, (255, 255, 255), (x, y), 30)

    def game_over(self, msg):
        self._game_over = True
        # fondo transparente
        s = pygame.Surface(self.size)
        s.set_alpha(200)
        s.fill((0, 0, 0))
        self.background.blit(s, (0, 0))
        # texto
        font = pygame.font.Font(None, 56)
        text = font.render(msg, 1, (255, 0, 255))
        textpos = text.get_rect(
            centerx=self.background.get_width()/2,
            centery=self.background.get_height()/2)
        self.background.blit(text, textpos)


	
	
def main(args):
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Tres en Raya')
    clock = pygame.time.Clock()
    scene_manager = SceneManager(initial_scene=args.e, music=args.m)
    game_over = False
    while not game_over:
        clock.tick(60)
        game_over = scene_manager.current_scene.process_input(scene_manager)
        scene_manager.current_scene.render(screen)
    scene_manager.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tres en Raya opciones.')
    parser.add_argument('-e', metavar='e', type=int, default=1, choices=[1,2,3], help='escena inicial')
    parser.add_argument('-m', action='store_false', default=True, help='sin música')
    args = parser.parse_args()
    main(args)

