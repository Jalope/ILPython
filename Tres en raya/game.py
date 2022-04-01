"""
Implementación del juego tres en ralla. Tendremos un máximo de 2 jugadores. Cada jugador tendrá un tipo de ficha (X y 0). 

Las condiciones de parada son: 
    1. No hay casillas vacías
    2. Hay tres fichas seguidas del mismo tipo (mismo jugador) ya sea en horizontal, vertical o diagonal. 
Para ganar debemos tener algún jugador en la condición de parada do

Habrá un table de dimensión 3x3 y cada vez que se coloca una ficha se comprueba si la partida ha terminado. 
"""
from telnetlib import GA
import pygame
import random 

#constantes de tamaño para la ventana del juego
ALTURA = 480
ANCHO = 360

#Tasa de refresco
FPS = 30

#inicializacion pygame y creacion de la ventana

class Ficha_jugador1(pygame.sprite.Sprite): 
    def __init__(self, player):
        super().__init__()
        self.imagen1 = pygame.image.load("ficha_jugador1.png")
        self.imagen2 = pygame.image.load("ficha_jugador2.png")

class Jugador(pygame.sprite.Sprite): 
    def __init__(self):
        super(Jugador, self).__init__()
        
class Casilla(pygame.sprite.Sprite): 
    def __init__(self, x, y, pos):
        super(Casilla, self).__init__()
        self.image = pygame.image.load("vacia.png")
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 75


class Game():
    def __init__(self): 
        self.jugador = [Jugador(i) for i in range(2)]
        self.continuar = True 

    def movimientos(self): 
        pass

    def estan_jugando(self): 
        return self.continuar

    def parar(self): 
        self.continuar = False

class Mostrar(): 
    def __init__(self, juego): 
        self.juego = juego
        self.screen = pygame.display.set_mode((ANCHO, ALTURA)) 
        self.reloj = pygame.time.Clock()
        self.titulo = pygame.display.set_caption("Tres en raya!")
        self.fondo = pygame.image.load('fondo.jpg')
        continuar = True
        pygame.init()

    def analizar_evento(self): 
        for event in pygame.event.get():
            print() 
        pass

    def refrescar(self): 
        pass
    
    def tick(self): 
        self.reloj.tick(FPS)
    
    @staticmethod
    def quit():
        pygame.quit()



def main(): 
    try: 
        juego = Game()
        mostrar = Mostrar(juego)

        while juego.estan_jugando():
            juego.movimientos()
            mostrar.analizar_evento()
            mostrar.refrescar()
            mostrar.tick()
    finally: 
        pygame.quit()

if __name__ == "__main__": 
    main() 

        