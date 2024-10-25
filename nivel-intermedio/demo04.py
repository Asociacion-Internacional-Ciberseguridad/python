try:
    with open('archivo_inexistente.txt', 'r') as archivo:
        contenido = archivo.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
finally:
    print("Esto se ejecuta siempre.")
