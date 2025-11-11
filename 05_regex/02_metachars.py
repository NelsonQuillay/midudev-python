###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especificos que tienen un significado especial en las expresiones regulares.  

import re

# 1. El punto (.)
# Coincidir con cualquier caracter excepto el salto de linea (\n)

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = "H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if (found):
  print(found)
else:
  print("No se ha encontrado el patrón")


text = "casa caasa cosa cisa cesa caua"
pattern = r"c.sa" # r esta indicando que estamos creando una expresion regular (Regex). El \s es un espacio en blanco. 
matches = re.findall(pattern, text)
print(matches)#['casa', 'cosa', 'cisa', 'cesa', 'causa']


# Cómo usar la barra invertida para anular el significado especial de un símbolo
text = "Mi casa es blanca. Y el coche es negro."
pattern = "." # ['M', 'i', ' ', 'c', 'a', 's', 'a', ' ', 'e', 's', ' ', 'b', 'l', 'a', 'n', 'c', 'a', '.', ' ', 'Y', ' ', 'e', 'l', ' ', 'c', 'o', 'c', 'h', 'e', ' ', 'e', 's', ' ', 'n', 'e', 'g', 'r', 'o', '.']
pattern = r"\." #['.', '.']

matches = re.findall(pattern, text)

print(matches)


# \d: coincide con cualquier dígito (0-9)

text = "El número de teléfono es 123456789"
found = re.findall(r'\d', text) #['1', '2', '3', '4', '5', '6', '7', '8', '9']
found = re.findall(r'\d\d\d', text) #['123', '456', '789']
found = re.findall(r'\d\d\d\d\d\d\d\d\d', text) #['123456789']
found = re.findall(r'\d{9}', text) #['123456789'] {9} se llama cuantificador, indicamos cuando digitos queremos buscar 

print(found) 

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34

text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: print(f"Encontré el número de teléfono {found.group()}")

# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found) #['e', 'l', '_', 'r', 'u', 'b', 'i', 'u', 's', '_', '6', '9']


# \s: Coincide con cualqueir espacio en blanco (espacio, tabulación, salto de línea)
text = "Hola mundo\n¿Cómo estás?\t" #\n salto de linea, \t tabulacion
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches) #[' ', '\n', ' ', '\t']  


# ^: Coincide con el principio de una cadena
username = "@423_name%22" 
pattern = r"^\w" # validar nombre de usuario

valid = re.search(pattern, username)
if valid:
  print("Nombre de usuario válido")   
else:
  print("Nombre de usuario inválido")


phone = "+34 688999999"
pattern = r"^\+\d{1,3} " #el espacio despues de la llave indica que debe haber un espacio despues del prefijo de país

valid = re.search(pattern, phone)

if valid: print("El número de teléfono es válido")
else: print("El número de teléfono no es válido") 


# $: Coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$"

valid = re.search(pattern, text)

if valid: print("La cadena es válida")
else: print("La cadena no es válida")

# EJERCICIO
# Valida que un correo sea de gmail
text = "miduga@gmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)

if valid: print("El correo es gmail válido")
else: print("El correo no es válido")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"


# \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"

found = re.findall(pattern, text)
print(found) #['casa', 'cosa', 'casa']


# |: Coincidr con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)