import threading

def imprimir_mensaje():
    print("Este es un mensaje desde otro hilo")

hilo = threading.Thread(target=imprimir_mensaje)
hilo.start()
hilo.join()
