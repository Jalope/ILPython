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
import numpy as np

#constantes de tamaño para la ventana del juego
ALTURA = 480
ANCHO = 360

#Tasa de refresco
FPS = 30

#inicializacion pygame y creacion de la ventana

class Jugador(): 
    def __init__(self, numero): 
        self.numero = numero 
        self.turno_P1 = 5 #El jugador que empieza a lo sumo tendrá 5 turnos
        self.turno_P2 = 5
        self.simbolo_P1 = -1
        self.simbolo_P2 = 1
    
    def get_posicion(self): 
        return self.pos

    def size(self): 
        return self.size

    def get_coordenadas_click (self): 
        self.x = int(self.pos[0] // (self.size[0] / 3))
        self.y = int(self.pos[1] // (self.size[1] / 3))

        
class Tablero(): 
    def __init__(self): 
        self.state = np.zeros((3,3))
    
    def movimiento_valido(self): 
        return [(i,j) for j in range(3) for i in range(3) if self.state[i,j] == 0]

    def update(self, simbolo, fila, columna): 
        if self.state[
            fila, columna] == 0:
            self.state[fila, columna] = simbolo 
        else: 
            raise ValueError("Casilla ocupada o fuera del tablero")
    
    def acabar_juego(self): 
        # comprobar filas y columnas
        if (self.state.sum(axis=0) == 3).sum() >= 1 or (self.state.sum(axis=1) == 3).sum() >= 1:
            return 1
        if (self.state.sum(axis=0) == -3).sum() >= 1 or (self.state.sum(axis=1) == -3).sum() >= 1:
            return -1 
        # comprobar diagonales
        diag_sums = [
            sum([self.state[i, i] for i in range(3)]),
            sum([self.state[i, 3 - i - 1] for i in range(3)]),
        ]
        if diag_sums[0] == 3 or diag_sums[1] == 3:
            return 1
        if diag_sums[0] == -3 or diag_sums[1] == -3:
            return -1        
        # empate
        if len(self.valid_moves()) == 0:
            return 0
        # seguir jugando
        return None
    
    def reset(self):
        self.state = np.zeros((3,3))


class Game():
    def __init__(self): 
        self.jugador = [Jugador(i) for i in range(2)]
        self.continuar = True 
        self.tablero = Tablero()

        def get_jugador(self, numero):
            l

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

        