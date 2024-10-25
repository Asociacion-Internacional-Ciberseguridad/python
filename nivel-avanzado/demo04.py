from contextlib import contextmanager

@contextmanager
def recurso():
    print("Entrando al contexto")
    yield
    print("Saliendo del contexto")

with recurso():
    print("Dentro del contexto")
