import pickle

data = {'nombre': 'Ana', 'edad': 25}
with open('data.pkl', 'wb') as archivo:
    pickle.dump(data, archivo)

with open('data.pkl', 'rb') as archivo:
    data_cargada = pickle.load(archivo)
    print(data_cargada)
