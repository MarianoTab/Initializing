import requests
import json

# URL de la API de prueba
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Realiza la solicitud GET a la API
    response = requests.get(url)
    response.raise_for_status() #verifica si hubo errores en la solicitud

    # Conviernte la respuesta en formato JSON
    data = response.json()

    # Guarda los datos en un archivo JSON
    with open("posts.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print ("Datos obtenidos y guardados en posts.json")
except requests.exceptions.RequestException as e:
    print (f"Error al obtener los datos: {e}")

