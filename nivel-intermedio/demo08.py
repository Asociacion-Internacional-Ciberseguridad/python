import json

data = {"nombre": "Juan", "edad": 25}
json_data = json.dumps(data)
print(json_data)

data_cargada = json.loads(json_data)
print(data_cargada["nombre"])
