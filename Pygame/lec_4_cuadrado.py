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

#variables para la animacion del cuadrado 
cord_x = 400
cord_y = 200

speed_x = 3
speed_y = 3

continuar = True 

while True: 
    for event in pygame.event.get():
        print(event) 
        if event.type == pygame.QUIT: 
            sys.exit()
    screen.fill(WHITE)

    #ZONA CON LA LOGICA DEL JUEGO
    #para que rebote tenemos que controlar las coordenadas, si no desaparecera de la pantalla
    #la cordenada x tiene que contar con el grosor del cuadrado
    if (cord_x > 820) or (cord_x < 0):   
        #invertimos la velocidad
        speed_x *= -1
    if (cord_y > 520) or (cord_y < 0):
        speed_y *= -1 

    cord_x += speed_x
    cord_y += speed_y

    ##--- ZONA DE DIBUJO
    pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80)) 
    ##--- 

    # ZONA DE ACTUALIZACION DE LA PANTALLA
    pygame.display.flip()
    #actualizaciones del reloj
    clock.tick(FPS)