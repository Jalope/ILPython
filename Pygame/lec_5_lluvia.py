import random
import pygame
import sys

#Definimos colores
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
GREEN = (0 , 255 , 0)
RED   = (255 , 0 , 0)
BLUE  = (0 , 0 , 255)

#Fotrogramas por segundo 
FPS = 60

pygame.init()  

size = (900, 600)

screen = pygame.display.set_mode(size)

#reloj para controlar las animaciones 
clock = pygame.time.Clock()

continuar = True 

coord_list = []
for i in range(60): 
    x = random.randint(0, 900)
    y = random.randint(0, 600)
    coord_list.append([x,y])

while continuar: 
    for event in pygame.event.get():
        print(event) 
        if event.type == pygame.QUIT: 
            sys.exit()
    
    screen.fill(WHITE)

    #ZONA CON LA LOGICA DEL JUEGO

    ##--- ZONA DE DIBUJO
    for coordinate in coord_list: 
        x = coordinate[0]
        y = coordinate[1]
        pygame.draw.circle(screen, RED, (x, y), 2)
        coordinate[1] += 1
        if coordinate[1] > 600 : 
            coordinate[1] = 0
    ##--- 

    # ZONA DE ACTUALIZACION DE LA PANTALLA
    pygame.display.flip()
    clock.tick(FPS)