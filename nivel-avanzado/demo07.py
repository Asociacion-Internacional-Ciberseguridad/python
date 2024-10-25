import asyncio

async def tarea(nombre, tiempo):
    print(f"Inicio de {nombre}")
    await asyncio.sleep(tiempo)
    print(f"Fin de {nombre}")

async def main():
    await asyncio.gather(tarea("Tarea 1", 2), tarea("Tarea 2", 1))

asyncio.run(main())
