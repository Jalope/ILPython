import pygame

screen = pygame.display.set_mode([900, 506])
clock = pygame.time.Clock()

running = True 

#donde ejecutemos debe estar la imagen
background = pygame.image.load("fondo.jpg").convert()

player = pygame.image.load("player.jpeg").convert()
#si la imagen es un png, para quitar el color que le pone por defecto pygame
player.set_colorkey([255, 255, 255]) #en este caso al no ser un png no queda perfecto 



while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    mous_pos = pygame.mouse.get_pos()
    x = mous_pos[0]
    y = mous_pos[1]

    screen.blit(background, [0,0])
    screen.blit(player, [x, y])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()