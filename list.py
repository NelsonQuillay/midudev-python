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
