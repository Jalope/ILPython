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

clock = pygame.time.Clock()

coord_x = 10
coord_y = 10

speed_x = 0 
speed_y = 0

continuar = True 

while continuar: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            continuar = False
        #EVENTOS DEL TECLADO 
        #Tiene que estar dentro del for ya que usaremos los eventos
        if event.type == pygame.KEYDOWN: #presionar la tecla
            if event.key == pygame.K_LEFT: #tecla de la izq. En la documentacion vienen todas las teclas --> http://www.pygame.org/docs/ref/key.html
                speed_x = -3
            if event.key == pygame.K_RIGHT:    
                speed_x = 3
            if event.key == pygame.K_DOWN: 
                speed_y = 3
            if event.key == pygame.K_UP:    
                speed_y = -3
    

        if event.type == pygame.KEYUP: #soltar la tecla
            if event.key == pygame.K_LEFT: 
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_DOWN: 
                speed_y = 0
            if event.key == pygame.K_UP:
                speed_y = 0
    


    screen.fill(WHITE)

    #ZONA CON LA LOGICA DEL JUEGO
    if coord_x > 800:
        coord_x = 800
    elif coord_x < 0:
        coord_x = 0
    else:  
        coord_x += speed_x
    
    if coord_y > 500: 
        coord_y = 500
    elif coord_y < 0:
        coord_y = 0
    else: 
        coord_y += speed_y

    ##--- ZONA DE DIBUJO
    pygame.draw.rect(screen, RED, (coord_x, coord_y, 100, 100)) 
    ##--- 

    # ZONA DE ACTUALIZACION DE LA PANTALLA
    pygame.display.flip()
    clock.tick(FPS)