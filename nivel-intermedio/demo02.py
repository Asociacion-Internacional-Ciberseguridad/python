class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra.")

perro = Perro()
perro.hacer_sonido()
