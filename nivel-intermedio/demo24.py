import multiprocessing

def proceso_func():
    print("Este es un proceso separado")

p = multiprocessing.Process(target=proceso_func)
p.start()
p.join()
