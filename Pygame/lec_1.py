import pygame
import sys #para rastrear eventos en la ventana 

#inicializamos la libreria
pygame.init()  

size = (800, 500)

#creamos la ventana
screen = pygame.display.set_mode(size)

#los juegos corren en un bucle infinitio 
continuar = True 

while True: 
    for event in pygame.event.get(): #bucle que rastrea todos los eventos del juego 
        #buscamos dentro de los eventos uno que sea cerrar la ventana (dentro de la libreria pygame es .QUIT)
        print(event) #--> Si ejecutamos vemos que se imprimen todos los evento como mover el ratón o hacer click 
        if event.type == pygame.QUIT: 
            #una vez encontrado ese evento le decimos lo que tiene que hacer, en este caso cerrar la ventana 
            sys.exit() 

