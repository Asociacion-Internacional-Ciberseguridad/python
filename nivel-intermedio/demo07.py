import re

patron = r"\d+"
texto = "Hay 123 números en esta cadena."
coincidencias = re.findall(patron, texto)
print(coincidencias)
