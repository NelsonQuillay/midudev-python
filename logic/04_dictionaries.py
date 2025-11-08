###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

from os import system
if system("clear") != 0: system("cls")

# ejemplo tipico de diccionario
persona = {
  "nombre": "nelson",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "facebook": "midudev"
  }
}

# para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])

# cambiar  valores
persona["nombre"] = "quillay"
persona["calificaciones"][2] = 10

print(persona["nombre"])
print(persona["calificaciones"][2])
print("\n")
print(persona)
print("\n")

# eliminar una propiedad
del persona["edad"]
print(persona)
print("\n")

es_estudiante = persona.pop("es_estudiante") 
print(f"es_estudiante: {es_estudiante}")
print("\n")
print(persona)
print("\n")

# sobreescribir un diccionario con otro diccionario
a = { "name": "nelson", "age": 25 }
b = { "name": "quillay", "es_estudiante": True }

a.update(b)
print(a)
print("\n")

# comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # True
print("\n")

# para obtener las claves/llave
print(persona.keys())
print("\n")

# para obtener los  valores
print(persona.values())
print("\n")

# para obtener clave y valor
print(persona.items()) 
print("\n")

for key, value in persona.items():
  print(f"{key}: {value}")

  