import pandas as pd

data = {'Nombre': ['Juan', 'Ana'], 'Edad': [28, 25]}
df = pd.DataFrame(data)
df.to_csv('archivo.csv', index=False)

df_cargado = pd.read_csv('archivo.csv')
print(df_cargado)
