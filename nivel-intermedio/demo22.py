import argparse

parser = argparse.ArgumentParser(description="Ejemplo de argparse")
parser.add_argument('numero', type=int, help="Número de entrada")
args = parser.parse_args()
print(f"El número ingresado es {args.numero}")

