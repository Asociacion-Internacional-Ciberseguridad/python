def decorador(func):
    def wrapper():
        print("Función decorada")
        func()
        print("Finaliza la función decorada")
    return wrapper

@decorador
def saludar():
    print("Hola Mundo")

saludar()
