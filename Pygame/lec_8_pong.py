from ast import While
import random
import pygame

#ventana
WIDHT = 900
HEIGHT = 600

#Definimos colores
BLACK     = (0 , 0 , 0)
WHITE     = (255 , 255 , 255)
GREEN     = (0 , 255 , 0)
RED       = (255 , 0 , 0)
RED_LIGHT = (255, 87, 51)
BLUE      = (0 , 0 , 255)

#raqueta
player_width = 15
player_height = 90



#players colocación inicial 
player1_x_coord = 50
player1_y_coord = (HEIGHT // 2) - (player_height // 2 )
player1_y_speed = 0 #vale cero de inicio pues depende del jugador

player2_x_coord = WIDHT - player1_x_coord - player_width
player2_y_coord = (HEIGHT // 2) - (player_height // 2 )
player2_y_speed = 0

#pelota
radious = 10
pelota_x = WIDHT // 2 
pelota_y = HEIGHT // 2
pelota_speed_x = 3 #no vale cero xq debe arrancar "sola"
pelota_speed_y = 3


#Fotrogramas por segundo 
FPS = 60

pygame.init()  

size = (WIDHT, HEIGHT)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()



continuar = True 

while continuar: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            continuar = False
        if event.type == pygame.KEYDOWN: 
            # Jugador 1
            if event.key == pygame.K_w: 
                player1_y_speed = -3
            if event.key == pygame.K_s: 
                player1_y_speed = 3
            
             # Jugador 2
            if event.key == pygame.K_UP: 
                player2_y_speed = -3
            if event.key == pygame.K_DOWN: 
                player2_y_speed = 3
        
        if event.type == pygame.KEYUP: 
            # Jugador 1
            if event.key == pygame.K_w: 
                player1_y_speed = 0
            if event.key == pygame.K_s: 
                player1_y_speed = 0
            
             # Jugador 2
            if event.key == pygame.K_UP: 
                player2_y_speed = 0
            if event.key == pygame.K_DOWN: 
                player2_y_speed = 0

    screen.fill(BLACK)

    #ZONA CON LA LOGICA DEL JUEGO
    if (player1_y_coord > HEIGHT - player_height): 
        player1_y_coord = HEIGHT - player_height
    elif (player1_y_coord < 0): 
        player1_y_coord = 0
    else: 
        player1_y_coord += player1_y_speed

    if (player2_y_coord > HEIGHT - player_height): 
        player2_y_coord = HEIGHT - player_height
    elif player2_y_coord < 0: 
        player2_y_coord = 0
    else: 
        player2_y_coord += player2_y_speed

    # Revisa si la pelota se sale del lado izquierdo  
    if (pelota_y > (HEIGHT - radious)) or (pelota_y < radious): 
        pelota_speed_y *= -1 
    
    # Revisa si la pelota se sale del lado derecho 
    if pelota_x > WIDHT or pelota_x < 0: 
        pelota_x = 400
        pelota_y = 300 
        #invertimos dirección 
        pelota_speed_x *= -1
        pelota_speed_y *= -1

    #pelota 
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    ##--- ZONA DE DIBUJO
    pygame.draw.line(screen, WHITE, (WIDHT//2, 0), (WIDHT//2, HEIGHT), 1)
    pygame.draw.line(screen, WHITE, )

    player1 = pygame.draw.rect(screen, GREEN, (player1_x_coord, player1_y_coord, player_width, player_height))
    player2 = pygame.draw.rect(screen, BLUE, (player2_x_coord, player2_y_coord, player_width, player_height))
    
    goal_zone_p1 = pygame.draw.rect(screen, RED_LIGHT, (0, 0, 50, HEIGHT))
    goal_zone_p2 = pygame.draw.rect(screen, RED_LIGHT, (WIDHT - 50, 0, 50, HEIGHT ))

    pelota = pygame.draw.circle(screen, WHITE, (pelota_x, pelota_y), radious)
    ##--- 

    # ZONA DE ACTUALIZACION DE LA PANTALLA
    pygame.display.flip()
    clock.tick(FPS)