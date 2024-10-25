def generador_cuadrados(limite):
    for i in range(limite):
        yield i ** 2

for numero in generador_cuadrados(5):
    print(numero)
