import random
import pygame



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 900
HEIGHT = 600

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

FPS = 60 

class Player(pygame.sprite.Sprite):
    def __init__(self, side, imagE):
        super().__init__()
        self.side = side
        self.image = pygame.image.load(imagE).convert()
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect() #(x,y)
        self.speed_x = 0
        self.speed_y = 0

    #le pasamos el parametro x que representa la velocidad
    def changespeed(self, x): 
        self.speed_x += x
    
    #encapsulamos 
    def update(self, player): 
        self.rect.x += self.speed_x
        player.rect.y = self.side


class Game(object):
    def __init__(self): 
        self.score_P1 = 0
        self.score_P2 = 0
        self.game_over = False
        self.all_sprite_list = pygame.sprite.Group()
        self.meteor_list = pygame.sprite.Group()
        self.laser_list1 = pygame.sprite.Group()
        self.laser_list2 = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()


        self.player1 = Player(510, "player1.png")
        self.player_list.add(self.player1)
        self.all_sprite_list.add(self.player1)

        self.player2 = Player(0, "player2.png")        
        self.player_list.add(self.player2)
        self.all_sprite_list.add(self.player2)

    def process_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return False 

            if event.type == pygame.KEYDOWN:
                if self.game_over: 
                        self.__init__() 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player1.changespeed(-3)
                if event.key == pygame.K_RIGHT:
                    self.player1.changespeed(3)

            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT:
                    self.player1.changespeed(3)
                if event.key == pygame.K_RIGHT:
                    self.player1.changespeed(-3)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player2.changespeed(-3)
                if event.key == pygame.K_d:
                    self.player2.changespeed(3)

            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_a:
                    self.player2.changespeed(3)
                if event.key == pygame.K_d:
                    self.player2.changespeed(-3)

        
        return True
    
    def run_logic(self): 
        if not self.game_over: 
            self.all_sprite_list.update()
            

        

    def display_frame(self, screen): 
        screen.fill(WHITE)

         #texto para game over 
        if self.game_over: 
            font = pygame.font.SysFont("serif", 25) #Fuente
            text = font.render("Game Over! Click to continue", True, BLACK) #Texto 
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2) #posicion del texto
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y]) #imprimirlo en la ventana del juego
        else: 
            self.all_sprite_list.draw(screen)

        for player in self.player_list: 
                self.player_list.update(player)

        self.all_sprite_list.draw(screen)
        pygame.display.flip()

def main(): 

    pygame.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    clock = pygame.time.Clock()
    running = True 
    
    game = Game()

    while running: 
        running = game.process_events()
        game.run_logic
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__": 
    main()