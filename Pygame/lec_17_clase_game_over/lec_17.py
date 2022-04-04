import pygame, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect()

    def update(self): 
        self.rect.y += 1
        
        if self.rect.y > SCREEN_HEIGHT: 
            self.rect.y = -10
            self.rect.x = random.randrange(SCREEN_WIDTH)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    
    def update(self): 
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]


class Game(object):
    def __init__(self): 
        self.score = 0
        self.game_over = False
        self.meteor_list = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()


        for i in range(50): 
            meteor = Meteor()
            meteor.rect.x = random.randrange(SCREEN_WIDTH)
            meteor.rect.y = random.randrange(SCREEN_HEIGHT)

            self.meteor_list.add(meteor)
            self.all_sprite_list.add(meteor)

        self.player = Player()
        self.all_sprite_list.add(self.player)

    def process_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if self.game_over: 
                    self.__init__()
        return True 

    def run_logic(self): 
        if not self.game_over: 
            self.all_sprite_list.update()
    
            meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

            for meteor in meteor_hit_list: 
                self.score += 1
                print(self.score)

            if len(self.meteor_list) == 0: 
                self.game_over = True 

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


        self.all_sprite_list.draw(screen)
        pygame.display.flip()

def main(): 
    pygame.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    running  = True 
    clock = pygame.time.Clock()

    game = Game()

    while running: 
        running = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit


if __name__ == "__main__": 
    main()