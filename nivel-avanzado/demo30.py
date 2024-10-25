def es_seguro(tablero, fila, col):
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    for i, j in zip(range(fila, len(tablero)), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    return True

def resolver_n_reinas(tablero, col):
    if col >= len(tablero):
        return True
    for i in range(len(tablero)):
        if es_seguro(tablero, i, col):
            tablero[i][col] = 1
            if resolver_n_reinas(tablero, col + 1):
                return True
            tablero[i][col] = 0
    return False

def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

n = 4
tablero = [[0] * n for _ in range(n)]
if resolver_n_reinas(tablero, 0):
    imprimir_tablero(tablero)
else:
    print("No tiene solución.")
