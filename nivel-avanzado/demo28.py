from collections import namedtuple

Persona = namedtuple('Persona', 'nombre edad')
persona = Persona(nombre="Ana", edad=30)
print(persona.nombre, persona.edad)
