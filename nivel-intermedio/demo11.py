class ContextoPersonalizado:
    def __enter__(self):
        print("Entrando al contexto")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saliendo del contexto")

with ContextoPersonalizado():
    print("Dentro del contexto")
