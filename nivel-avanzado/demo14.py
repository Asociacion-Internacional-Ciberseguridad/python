from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
    activo: bool = True

persona = Persona(nombre="Juan", edad=28)
print(persona)
