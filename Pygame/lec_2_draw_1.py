import pygame
import sys

#Definimos colores
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
GREEN = (0 , 255 , 0)
RED   = (255 , 0 , 0)
BLUE  = (0 , 0 , 255)

pygame.init()  

size = (800, 500)


screen = pygame.display.set_mode(size)


continuar = True 

while True: 
    for event in pygame.event.get():
        print(event) 
        if event.type == pygame.QUIT: 
            sys.exit()
    
    #pintamos la pantalla
    screen.fill(WHITE)
    
    ##--- ZONA PARA DIBUJAR

    #linea recta 
    pygame.draw.line(screen, GREEN, [0, 100], [100, 100], 5)
    pygame.draw.line(screen, RED, [100, 100], [250, 25], 2)
    #para ver todo lo que podemos dibujar con pygame.draw --> https://www.pygame.org/docs/ref/draw.html
    pygame.draw.circle(screen, RED, (200,200), 100, 1)
    ##---
        
    #actualizamos para que pase del color negro por defecto a blanco 
    pygame.display.flip()