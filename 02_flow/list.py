import os
os.system("clear")

lista1 = [1, 2, 3, 4, 5]
lista2 = ["manzana", "pera", "banana"]
lista3 = [True, 3.1416, "name", 3]
lista_vacia = []
lista_de_lista = [[1, 2], [3, 4]]

#aceso a elemento por indice

'''print(lista2[0])
print(lista2[1])
print(lista2[-1]) # a la ultima posicion
print(lista2[-2]) # a la ante ultima posicion
print(lista_de_lista[1][0]) #3'''

#slicing (rebanado) de listas
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [4, 5]
print(lista1[:]) # hace una copia de la lista [1, 2, 3, 4, 5]

#!print(lista1["desde":"hasta":"paso"])
lista_larga = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_larga[0:10:2]) #[1, 3, 5, 7, 9]
print(lista_larga[::3]) #[1, 4, 7, 10]
print(lista_larga[::-1]) # te devuelve la lista la reverso [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# modificar la lista
lista_larga [0] = 50
print(lista_larga) # [50, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#añadir elementos a la lista
lista_larga = lista_larga + [20, 21, 22] # el + me va a concatenar los elementos
print(lista_larga)

#añadir forma las corta
lista_larga += [30, 31, 32]

#longitud de la lista con len
print("la longitud de la lista es: ",len(lista_larga)) # la longitud de la lista es:  16

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]