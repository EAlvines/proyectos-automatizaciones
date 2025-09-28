#Conectar con API y Revisar la data
import requests
import json

url = "https://randomuser.me/api/"
responses = requests.get(url)

# Validamos que haya funcionado la conexion
if responses.status_code == 200:
    data = responses.json()
    print(json.dumps(data, indent=4))  # Imprime todo el contenido del JSON con identado
else:
    print("error")
