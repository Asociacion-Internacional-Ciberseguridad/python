import random

def estimar_pi(n):
    adentro_circulo = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            adentro_circulo += 1
    return (adentro_circulo / n) * 4

print(estimar_pi(100000))
