import timeit

codigo = """
numeros = [x for x in range(100)]
"""
tiempo = timeit.timeit(codigo, number=1000)
print(tiempo)
