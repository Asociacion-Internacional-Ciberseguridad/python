import multiprocessing

def tarea(n):
    return n * n

with multiprocessing.Pool(4) as pool:
    resultado = pool.map(tarea, [1, 2, 3, 4])
    print(resultado)
