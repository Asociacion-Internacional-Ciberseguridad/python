import threading

contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100000):
        with lock:
            contador += 1

hilos = [threading.Thread(target=incrementar) for _ in range(2)]
for hilo in hilos:
    hilo.start()
for hilo in hilos:
    hilo.join()

print(f"Contador final: {contador}")
