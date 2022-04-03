import pygame

screen = pygame.display.set_mode([900, 506])
clock = pygame.time.Clock()

running = True 

#donde ejecutemos debe estar la imagen
background = pygame.image.load("fondo.jpg").convert()

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    screen.blit(background, [0,0])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()