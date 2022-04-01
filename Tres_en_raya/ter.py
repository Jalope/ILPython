from concurrent.futures import process
from curses import mouseinterval
import random
from turtle import screensize

import pygame
from enum import Enum

class Escenas(Enum): 
    MENU = 1
    JUEGO = 2

class SceneManager(): 
    def __init__(self, escena_inicial = 1): 

        escenas = {}
        escenas[Escenas.MENU] = StartMenu()
        escenas[Escenas.JUEGO] = GameScene()
        self.escenas = escenas
        self.escena_actual = escenas[Escenas(escena_inicial)]
        self.escena_actual.start()
    
    def cambiar_escena(self, nueva_escena): 
        if self.escenas[nueva_escena] != self.escena_actual:
            self.escena_actual.stop()
            self.escena_actual = self.escenas[nueva_escena]
            self.escena_actual.start()

    

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Tres en RaYa!")
    clock = pygame.time.Clock()
    continuar = True 
    while continuar: 
        continuar = scene_manager.current_scene.process_input(scene_manager)
        scene_manager.current_scene.render(screen)
    scene_manager.strop()


if __name__ == "__main()__": 
    main()
    