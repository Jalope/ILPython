#tablero1 = [[1,1,-1],[-1,1,1],[-1,1,1]]
#tablero2 = [[1,1,-1],[-1,-1,1],[-1,1,1]]


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

#b1 = comprobar_diagonal(tablero1, 3)
#b2 = comprobar_diagonal(tablero2, -3)
#print(b1, b2)