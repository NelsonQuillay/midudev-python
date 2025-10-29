#! FOR
#! Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista

# Iterar una lista

frutas = ["manzana", "naranja", "banana", "pomelo", "pera"]

for fruta in frutas:
    print(fruta)

#iterart cualquier cosa que sea iterable

cadena = "Quillay"

for caracter in cadena:
    print(caracter)


# ENUMERATE()
frutas = ["manzana", "naranja", "banana", "pomelo", "pera"]
for index, fruta in enumerate(frutas):
    print(f"{fruta} esta en la posicion {index} de la lista")


#bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for num in numeros:
        print(f"{letra} {num}")

#break
animales = ["perro", "gato", "pajaro", "conejo", "pez"]

for idx, animal in enumerate(animales):
    #   print(animal)
    if animal == "conejo":
        print(f"El {animal} esta escondido en el indice {idx} de la lista")
        break

#continue
animales = ["perro", "gato", "pajaro", "conejo", "pez"]

for animal in animales:
    #if animal == "conejo":
        #continue
    if animal == "conejo": continue

    print(animal)

#compresion de lista (list comprehension)
animales = ["perro", "gato", "pajaro", "conejo", "pez"]
animales_mayus = [animal.upper() for animal in animales] #<- (list comprehension) hacer una lista en una sola linea
print(animales_mayus)


#compresion de lista con condicional
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num %2 == 0]
#pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num %2 == 0]
print(pares) #[2, 4, 6, 8, 10]

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")