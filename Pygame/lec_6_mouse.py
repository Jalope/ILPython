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

#definimos la visibilidad del puntero del ratón con 1 o 0 o True o False
pygame.mouse.set_visible(False)

while continuar: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    screen.fill(WHITE)

    #ZONA CON LA LOGICA DEL JUEGO
    #capturar por donde se mueve el ratón, se genera como una tupla  
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    x = mouse_pos[0]
    y = mouse_pos[1]
    ##--- ZONA DE DIBUJO
    pygame.draw.rect(screen, RED, (x,y, 100, 100)) 
    ##--- 

    # ZONA DE ACTUALIZACION DE LA PANTALLA
    pygame.display.flip()
    clock.tick(FPS)