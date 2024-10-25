class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creando la clase {name}")
        return super().__new__(cls, name, bases, dct)

class MiClase(metaclass=Meta):
    pass

obj = MiClase()
