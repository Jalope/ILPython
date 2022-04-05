import numpy as np

#LOGICA DEL TRES EN RAYA
class Tablero(): 
    def __init__(self): 
        self. tablero = np.zeros((3,3)) 
        
class Jugador1(): 
    def __init__(self, tablero):
        self.fila = int(input("Introduce la fila que quieres marcar: "))
        self.columna = int(input("Introduce la columna que quieres marcar: "))
        self.jugada = (self.fila, self.columna)
        self.repetir = True   

    def jugada_P1(self): 
        while self.repetir: 
            aux = "Marcaras la casilla: ", self.jugada, ".", "¿Estas seguro? (S/N)"
            respuesta = str(input(aux)) 
            respuesta = respuesta.upper()
            if respuesta == "N":
                self.fila = int(input("Introduce la fila que quieres marcar: "))
                self.columna = int(input("Introduce la columna que quieres marcar: "))
                self.jugada = (self.fila, self.columna)
                self.repetir = True
            else: 
                self.repetir = self.__class_.comprobar_jugada(tablero, self.jugada)    

        if self.repetir == False: 
            tablero[self.jugada[0]][self.jugada[1]] = 1

    def comprobar_jugada(self, tablero, self.jugada): 
        pass


class Game(): 
    def __init__(self): 
        self.tablero = Tablero()





    while running: 
        if turno == 1: 
            jugada_P1(tablero)
            game_over = comprobar_game_over(tablero, 3)
            if game_over == True: 
                print("Ha ganado el Jugador 1")
                break 
            else: 
                print(game_over)
                turno = -1
                print("CAMBIO DE TURNO")
        else: 
            jugada_P2(tablero)
            game_over = comprobar_game_over(tablero, -3)
            if game_over == True: 
                running == False
                print("Ha ganado el Jugador 2")
                break
            else: 
                turno = 1
                print("CAMBIO DE TURNO")


if __name__ == "__main__": 
    main()