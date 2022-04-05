import numpy as np

#LOGICA DEL TRES EN RAYA

def comprobar_fila(tablero, condicion): 
    s1, s2, s3 = 0, 0, 0
    n = 0
    while len(tablero) != n: 
        s1 += tablero[0][n]
        s2 += tablero[1][n]
        s3 += tablero[2][n]
        n += 1 
    
    if s1 == condicion or s2 == condicion or s3 == condicion: 
        return True
    else: 
        return False

def comprobar_columna(tablero, condicion): 
    s1, s2, s3 = 0, 0, 0
    n = 0
    while len(tablero) != n: 
        s1 += tablero[n][0]
        s2 += tablero[n][1]
        s3 += tablero[n][2]
        n += 1 
    
    if s1 == condicion or s2 == condicion or s3 == condicion: 
        return True
    else: 
        return False

def comprobar_diagonal(tablero, condicion): 
    s1, s2 = 0, 0
    n = 0
    
    dM_i, dM_j = 0, 0 #fila y columna diagonal mayor
    
    dm_i = 2 #fila y columna diagonal menor
    dm_j = 0 

    while len(tablero) != n: 
        s1 += tablero[dM_i][dM_j]
        dM_i += 1
        dM_j += 1

        s2 += tablero[dm_i][dm_j]
        dm_i -= 1
        dm_j += 1

        n += 1 
    
    if s1 == condicion or s2 == condicion:
        return True
    else: 
        return False


def jugada_P1(tablero): 
    fila = int(input("Introduce la fila que quieres marcar: "))
    columna = int(input("Introduce la columna que quieres marcar: "))
    jugada = (fila, columna)
    repetir = True 
    
    while repetir: 
        aux = "Marcaras la casilla: ", jugada, ".", "¿Estas seguro? (S/N)"
        respuesta = str(input(aux)) 
        respuesta = respuesta.upper()
        if respuesta == "N":
            fila = int(input("Introduce la fila que quieres marcar: "))
            columna = int(input("Introduce la columna que quieres marcar: "))
            jugada = (fila, columna)
            repetir = True
        else: 
            repetir = comprobar_jugada(tablero, jugada)    

    if repetir == False: 
        tablero[jugada[0]][jugada[1]] = 1

    print(tablero)

    return jugada 

def jugada_P2(tablero): 
    fila = int(input("Introduce la fila que quieres marcar: "))
    columna = int(input("Introduce la columna que quieres marcar: "))
    jugada = (fila, columna)
    repetir = True 
    
    while repetir: 
        aux = "Marcaras la casilla: ", jugada, ".", "¿Estas seguro? (S/N)"
        respuesta = str(input(aux)) 
        respuesta = respuesta.upper()
        if respuesta == "N":
            fila = int(input("Introduce la fila que quieres marcar: "))
            columna = int(input("Introduce la columna que quieres marcar: "))
            jugada = (fila, columna)
            repetir = True
        else: 
            repetir = comprobar_jugada(tablero, jugada)    

    if repetir == False: 
        tablero[jugada[0]][jugada[1]] = -1

    print(tablero)

    return jugada 

def comprobar_jugada(tablero, jugada): 
    if tablero[jugada[0]][jugada[1]] == 0: 
        print("Jugada válida")
        return False
    else: 
        print("Jugada no válida")
        return True

def comprobar_game_over(tablero, condicion):
    a = comprobar_fila(tablero, condicion)
    b = comprobar_columna(tablero, condicion)
    c = comprobar_diagonal(tablero, condicion)

    if (a == True) or (b == True) or (c == True): 
        return True 
    else:
        return False 


def main():
    running = True 
    tablero = np.zeros((3,3))
    turno = 1
    game_over = False

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