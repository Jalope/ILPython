import random
from numpy import place
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 900
HEIGHT = 600


pygame.init()


screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
running = True 
score = 0 

#clases
#subclase de Sprite 

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.image.set_colorkey(BLACK)
        #necesitamos la siguiente variable para posicionar el sprite 
        self.rect = self.image.get_rect()

    def update(self): 
        self.rect.y -= 5 

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)
        #necesitamos la siguiente variable para posicionar el sprite 
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        #necesitamos la siguiente variable para posicionar el sprite 
        self.rect = self.image.get_rect()
    
    #encapsulamos 
    def update(self): 
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = 510

        if player.rect.x > WIDTH - (33*3):
            player.rect.x = WIDTH - (33*3)

all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()




player = Player()
all_sprite_list.add(player)

for i in range(50): 
    meteor = Meteor()
    meteor.rect.x = random.randrange(880)
    meteor.rect.y = random.randrange(450)
    
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)


pygame.mouse.set_visible(False)

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    #cada vez que pulso sale un laser 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            laser = Laser()
            laser.rect.x = player.rect.x + 45
            laser.rect.y = player.rect.y - 20 
            
            laser_list.add(laser)
            all_sprite_list.add(laser)



    all_sprite_list.update()

    for laser in laser_list: 
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)
        for meteor in meteor_hit_list: 
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score +=1 
            print(score)
        
        if laser.rect.y < -10: 
            all_sprite_list.remove(laser)
            laser_list.remove(laser)


    screen.fill(WHITE)
    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()