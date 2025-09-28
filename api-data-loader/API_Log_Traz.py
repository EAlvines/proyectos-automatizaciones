#CRUD CON TRAZABILIDAD: Scrip que exporta la data con un registro de acciones

import requests
import pandas as pd
from datetime import datetime

#definir la URL
url = "https://jsonplaceholder.typicode.com/users"

#Datos a enviar
usuarios = [{"name": "Lola Torres", "email": "ltorres@gmail.com", "username": "ltorres"},
            {"name": "Kevin Perez", "email": "kperez@gmail.com", "username": "kperez"}]

#Listas
respuestas = []
logs = []

#Función de trazabilidad
def registro(accion, detalle, status_code):
    logs.append({
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "accion": accion,
        "detalle": detalle,
        "status_code": status_code
    })

#Crear Usuarios 
for usuario in usuarios:
    response = requests.post(url, json=usuario)
    if response.status_code == 201:
        print(f"Usuario creado: {usuario['name']}")
        respuestas.append(response.json())
        registro("CREAR", f"Usuario creado {usuario['name']}", response.status_code)
    else:
        print(f"error al crear usuario {usuario['name']}")
        registro("CREAR_ERROR", f"No se pudo crear usuario {usuario['name']}", response.status_code)

#LEER Usuarios
response = requests.get(url)
if response.status_code == 200:
    registro("VISTO", f"Usuarios leidos correctamente. Total: {len(response.json())}", response.status_code)
else:
    registro("VISTO_ERROR", f"No se pudo leer lista de usuarios", response.status_code)

#ACTUALIZAR el primer registro
if respuestas:
    usuario_id = respuestas[0]['id']
    nuevo_dato = {"name": "Lola Torres actualizado"}
    response = requests.put(f"{url}/{usuario_id}", json=nuevo_dato)
    if response.status_code == 200:
        registro("Actualizar", f"Usuario {usuario_id} actualizado", response.status_code)
    else:
        registro("Actualizar_error", f"Usuario {usuario_id} no se pudo actualizar", response.status_code)

#Eliminar el segundo usuario
if len(respuestas)  > 1:  #para asegurarnos de que hay más de 1 registro 
    usuario_id = respuestas[1]['id']
    response = requests.delete(f"{url}/{usuario_id}")
    if response.status_code == 200:
        registro("Eliminar", f"usuario {usuario_id} eliminado", response.status_code)
    else:
        registro("Eliminar_error", f"usuario {usuario_id} no pudo ser eliminado", response.status_code)

#Guardar los datos en excel
df = pd.DataFrame(respuestas)
df.to_excel("Lista_usuarios.xlsx", index=False)

#guardar la trazabilidad
df_logs = pd.DataFrame(logs)
df_logs.to_excel("LOGS.xlsx", index=False)

print("Archivos creados con éxito")