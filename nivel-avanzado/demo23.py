def crear_clase(nombre, atributos):
    return type(nombre, (object,), atributos)

Persona = crear_clase('Persona', {'nombre': 'Juan', 'edad': 28})
persona = Persona()
print(f"{persona.nombre}, {persona.edad}")
