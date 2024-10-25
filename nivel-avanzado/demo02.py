def decorador_con_parametros(texto):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Texto: {texto}")
            return func(*args, **kwargs)
        return wrapper
    return decorador

@decorador_con_parametros("Ejemplo avanzado")
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Juan")
