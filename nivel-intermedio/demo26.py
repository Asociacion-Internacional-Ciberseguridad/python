class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

personas = [Persona("Ana", 30), Persona("Juan", 25)]
personas_ordenadas = sorted(personas, key=lambda p: p.edad)
for persona in personas_ordenadas:
    print(f"{persona.nombre}: {persona.edad}")
