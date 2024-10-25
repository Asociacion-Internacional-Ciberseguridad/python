class Matematica:
    @staticmethod
    def suma(a, b):
        return a + b

    @classmethod
    def mensaje(cls):
        return "Esto es un mensaje de la clase Matematica"

print(Matematica.suma(3, 4))
print(Matematica.mensaje())
