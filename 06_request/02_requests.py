# Cómo hacer peticiones a APIs con Python
# con y sin dependencias

# 1. Sin dependencias (díficil y sin dependencias)
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts/"

try:
    response = urllib.request.urlopen(api_posts) # Haciendo la petición GET
    data = response.read() # Lee el contenido de la respuesta
    json_data = json.loads(data.decode("utf-8")) # Convierte la respuesta en JSON
    print(json_data) # Imprime la respuesta en formato JSON
    response.close() # Cierra la conexión
except urllib.error.URLError as e:
    print(f"Error al hacer la petición: {e}")   

# 2. Con dependencia = (requests)

import requests

print("\nGET:") # Haciendo una petición GET
api_posts = "https://jsonplaceholder.typicode.com/posts/" # URL de la API
response = requests.get(api_posts) # Haciendo la petición GET
#print(response.json()) # Imprime la respuesta en formato JSON
json = response.json() # Guarda la respuesta en una variable
print(json[0]) # Imprime el primer elemento de la respuesta


# 3 un POST con requests
print("\nPOST:") # Haciendo una petición POST

'''api_posts = "https://jsonplaceholder.typicode.com/posts/" # URL de la API

input = {
    "title": "Nelson",
    "body": "Quillay",
    "userId": 26
} # Datos a enviar en la petición POST

response = requests.post(api_posts, json = input) # Haciendo la petición POST'''

try:
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts/",
        json = {
            "title": "Nelson",
            "body": "Quillay",
            "userId": 26
        }
    ) 

    print(response.json()) #
    print(response.status_code) # Imprime el código de estado de la respuesta

except requests.exceptions.RequestException as e:
    print(f"Error al hacer la petición: {e}")   

# 4. Un PUT
print("\nPUT:") # Haciendo una petición PUT

try:
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",#/posts/1 para actualizar el post con id 1
        json = {
            "title": "fooball",
            "body": "bar",
            "userId": 1,
        }
    )
    print(response.json()) #
    print(response.status_code) # Imprime el código de estado de la respuesta

except requests.exceptions.RequestException as e:
    print(f"Error al hacer la petición: {e}")

# un PATCH solo para actualizar un campo del objeto
print("\nPATCH:") # Haciendo una petición PATCH
try:
    response = requests.patch(
        "https://jsonplaceholder.typicode.com/posts/1",#/posts/1 para actualizar el post con id 1
        json = {
            "title": "Hectorrrrrr",
        }
    )
    print(response.json()) #
    print(response.status_code) # Imprime el código de estado de la respuesta
except requests.exceptions.RequestException as e:
    print(f"Error al hacer la petición: {e}")   

# Usar la API de GPT-4o de OpenAI
# Ref: https://platform.openai.com/docs/api-reference/making-requests

import os
import json
import requests

# ...existing code...

# Reemplazado: no dejar la clave en claro en el repositorio
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

def call_openai_gpt(api_key, prompt):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])

# Llamar a la API de DEEPSEEK

import json

DEEPSEEK_API_KEY = "REDACTED_DEEPSEEK_KEY"

def call_deepseek(api_key, prompt):
  url = "https://api.deepseek.com/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  print(response.json())
  return response.json()

api_response = call_deepseek(DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])
