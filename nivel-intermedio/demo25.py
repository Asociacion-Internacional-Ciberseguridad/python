class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo} de {self.autor}"

    def __repr__(self):
        return f"Libro({self.titulo}, {self.autor})"

libro = Libro("1984", "George Orwell")
print(libro)
