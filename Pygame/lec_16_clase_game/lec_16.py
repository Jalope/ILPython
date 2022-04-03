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
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)
        #necesitamos la siguiente variable para posicionar el sprite 
        self.rect = self.image.get_rect()

    def update(self): 
        self.rect.y += 1
        #desaparecen por abajo y nacen arriba (fuera de ventana). La aparición es aleatoria
        if self.rect.y > HEIGHT: 
            self.rect.y = -10
            self.rect.x = random.randrange(WIDTH)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        #necesitamos la siguiente variable para posicionar el sprite 
        self.rect = self.image.get_rect()
    
    #encapsulamos 
    def update(self): 
        for meteor in meteor_list: 
            meteor.rect.y += 1

#lista que contiene a los meteoros
meteor_list = pygame.sprite.Group()

#lista que contiene todos los sprites que permite poder dibujarlos con un solo metodo (linea 74)
all_sprite_list = pygame.sprite.Group()

for i in range(50): 
    meteor = Meteor()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(600)

    #lo guardamos en la lista 
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    mous_pos = pygame.mouse.get_pos()
    player.rect.x = mous_pos[0]
    player.rect.y = mous_pos[1]

    #mover los meteoros de arriba hacia abajo. Pero esto no tiene mucho sentido. Es mejor encapsularlo  
    #for meteor in meteor_list: 
    #    meteor.rect.y += 1 

    #El true lo que hace es eliminar cuando hay una colision 
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
    for meteor in meteor_hit_list: 
        score +=1 
        print(score)

    #la lista tiene meteoros y players pero como ambos tiene metodo update python sabe a cual llamar en cada caso 
    all_sprite_list.update()

    screen.fill(WHITE) 
    screen.blit(screen, [player.rect.x, player.rect.y])

    #dibujamos los meteoros 
    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()