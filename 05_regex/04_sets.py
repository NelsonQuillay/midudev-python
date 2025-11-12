import re

# [:] Coincide con cualquier caracter dentro de los corchetes

#username = "rub.$ius_69+"
#pattern = r"[\w._%+-]+" # El nombre de usuario es válido : rub.

#username = "rub.$ius_69+"
#pattern = r"^[\w._%+-]+$" # El nombre de usuario no es válido

username = "rub.ius_69+"
pattern = r"^[\w._%+-]+$" # El nombre de usuario es válido : rub.ius_69+

match = re.search(pattern, username)
if match:
  print("El nombre de usuario es válido: ", match.group())
else:
  print("El nombre de usuario no es válido")


# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches) #['o', 'a', 'u', 'o']


# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches) #['H', 'l', ' ', 'm', 'n', 'd']  


# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man ran tfan ñan ban an matman"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches) #['man', 'fan', 'ban', 'man']

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "man ran tfan ñan ban an matman"
pattern = r"\b[mfb]an\b"
matches = re.findall(pattern, text)
print(matches) #['man', 'ban']

text = "242"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches) #['4']


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

email = "lo.que+sea@shopping.online"
#pattern = r"/[w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}/" # Email no válido
#pattern = r"/[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}/" # Email válido
pattern = r"^[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}$" # Email válido:  ['lo.que+sea@shopping.online']
match = re.findall(pattern, email)
if match:
  print("Email válido: ", match)        
else:
  print("Email no válido")

email = "michael@gov.co.uk"
#pattern = r"/[w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}/" # Email no válido
pattern = r"^[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}$" #Email válido:  ['michael@gov.co.uk']
match = re.findall(pattern, email)
if match:
  print("Email válido: ", match)        
else:
  print("Email no válido")