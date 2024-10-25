from concurrent.futures import ThreadPoolExecutor

def tarea(n):
    return n * n

with ThreadPoolExecutor(max_workers=4) as executor:
    resultados = list(executor.map(tarea, range(10)))
    print(resultados)
