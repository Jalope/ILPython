import pygame
import sys

#Definimos colores
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
GREEN = (0 , 255 , 0)
RED   = (255 , 0 , 0)
BLUE  = (0 , 0 , 255)

pygame.init()  

size = (900, 600)


screen = pygame.display.set_mode(size)


continuar = True 

while True: 
    for event in pygame.event.get():
        print(event) 
        if event.type == pygame.QUIT: 
            sys.exit()
    screen.fill(WHITE)
    ##--- ZONA DE DIBUJO
    
    #Empezamos en 300, acabamos en 900 y vamos de 300 en 300 pixeles
    for x in range(300, 900, 300): 
        #pygame.draw.rect(screen, BLACK, (x, 230, 50, 50), 1)
        pygame.draw.line(screen, BLACK, (x, 50), (x, 550), 10)
    
    #Empezamos en 200, acabamos en 600 y vamos de 200 en 200 pixeles
    for y in range(200,600, 200): 
        pygame.draw.line(screen, BLACK, (50,y), (850,y), 10)    
    ##--- 
    pygame.display.flip()