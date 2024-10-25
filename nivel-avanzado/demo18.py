class ColaConPilas:
    def __init__(self):
        self.pila1 = []
        self.pila2 = []

    def encolar(self, valor):
        self.pila1.append(valor)

    def desencolar(self):
        if not self.pila2:
            while self.pila1:
                self.pila2.append(self.pila1.pop())
        return self.pila2.pop()

cola = ColaConPilas()
cola.encolar(1)
cola.encolar(2)
print(cola.desencolar())  # Imprime 1
