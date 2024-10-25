class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

persona = Persona("Ana")
persona.nombre = "Juan"
print(persona.nombre)
