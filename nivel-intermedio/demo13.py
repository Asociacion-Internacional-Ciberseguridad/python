from functools import reduce

numeros = [1, 2, 3, 4]
resultado = reduce(lambda x, y: x + y, numeros)
print(resultado)