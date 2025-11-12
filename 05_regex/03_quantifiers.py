###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

import re

# *: Puede aparecer 0 o más veces
text = "aaabax1aaaaa"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches) #['aaa', '', 'a', '', '', 'aaaaa', '']

# Ejercicio 1:
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?
text = "aaabax1aaaaa aaaaaab ab bb b cb abba"
pattern = "a*b"
matches = re.findall(pattern, text)
print(matches) #['aaab', 'aaaaaab', 'ab', 'b', 'b', 'b', 'b', 'ab', 'b']


# +: ¿Cuantas palabras tienen una a mas veces "a" y después una b? 
text = "aaabax1aaaaa aaaaaab ab bb b cb abba"
pattern = "a+b"
matches = re.findall(pattern, text)
print(matches) #['aaab', 'aaaaaab', 'ab', 'ab']

# -> ?: ¿Cuantas palabras tienen de 0 o una vez "a" y después una b? 
text = "aaabax1aaaaa aaaaaab ab bb b cb abba"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches) #['ab', 'ab', 'ab', 'b', 'b', 'b', 'b', 'ab', 'b']

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
#pattern = r"(\+34 )?(\d{9})" #[('+34 ', '688999999')]
pattern = r"\+34? \d{9}" #['+34 688999999']
matches = re.findall(pattern, phone)        
print(matches) 


# {n}: Exactamente n veces
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)

print(matches) #['aaa', 'aaa', 'aaa']

# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches) #['uu', 'uuu']

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches) #['casa', 'árbol', 'león', 'cinco']

# Ejercicio
# Encuentra las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches) # ['fantastico', 'murcielago'] 