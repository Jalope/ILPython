import pygame, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60

class Cruz(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cruz.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.turn = 1
        self.symbol = 1
        
    
    def update(self): 
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]

class Circulo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cirulo.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.turn = -1

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cruz.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.turn = 1

    
    def update(self): 
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("circulo.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.turn = 2    
    def update(self): 
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]




class Game(object):
    def __init__(self): 
        self.score = 0
        self.game_over = False
        self.player_list = pygame.sprite.Group()
        

        self.player1 = Player1()
        self.player2 = Player2()
        self.player_list.add(self.player1)
        self.player_list.add(self.player2)
        
        self.cruz_list = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()


    def process_events(self, turn): 

        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if self.game_over: 
                    self.__init__()

            if turn == 1: 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    cruz = Cruz()
                    x = int(event.pos[0] // (SCREEN_WIDTH // 3))
                    y = int(event.pos[1] // (SCREEN_HEIGHT // 3))
                    if ok_position(x,y): 
                        
                    self.cruz_list.add(cruz)
                    self.all_sprite_list.add(cruz)
                    turn = -1
                    
                
        return True 


    def run_logic(self): 
        if not self.game_over: 
            self.all_sprite_list.update()
    

    def display_frame(self, screen): 
        screen.fill(WHITE)
        for x in range(300, 900, 300): 
            pygame.draw.line(screen, BLACK, (x, 50), (x, 550), 10)
        
        for y in range(200,600, 200): 
            pygame.draw.line(screen, BLACK, (50,y), (850,y), 10)    
        

        #texto para game over 
        if self.game_over: 
            font = pygame.font.SysFont("serif", 25) #Fuente
            text = font.render("Game Over! Click to continue", True, BLACK) #Texto 
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2) #posicion del texto
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y]) #imprimirlo en la ventana del juego
        else: 
            self.all_sprite_list.draw(screen)


        self.all_sprite_list.draw(screen)
        pygame.display.flip()




def main(): 
    pygame.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    running  = True 
    clock = pygame.time.Clock()

    game = Game()

    turn = 1 

    while running: 
        running = game.process_events(turn)
        game.run_logic()
        game.display_frame(screen)
        clock.tick(FPS)
    pygame.quit


if __name__ == "__main__": 
    main()