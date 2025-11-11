import os
os.system("clear")

lista1 = [1, 2, 3, 4, 5]

lista1.append(6)#agregar un elemento al final de la lista
#print(lista1)

lista1.insert(3, 99)# el primer numero indica donde vas a insertar el nuevo valor y el segundo que valor va a ser
#print(lista1) #[1, 2, 3, 99 , 4, 5, 6]


lista1.extend(["muchos", "elementos", "al final", "de la lista",]) #se debe colocar corchetes 
#print(lista1) #[1, 2, 3, 99, 4, 5, 6, 'muchos', 'elementos', 'al final', 'de la lista']

lista1.remove(99) # elimina la primera cuicidencia
#print(lista1) #[1, 2, 3, 4, 5, 6, 'muchos', 'elementos', 'al final', 'de la lista']

lista1.pop() #elimina el ultimo de la lista y de lo devuelve. valor por defecto pop(-1) o se puede ingresar el indice que se desea eliminar ej: pop(2) [3]
print(lista1) #[1, 2, 3, 4, 5, 6, 'muchos', 'elementos', 'al final']

ultimo = lista1.pop() #elimina el ultimo de la lista y de lo devuelve
print(ultimo) #al final
print(lista1) #[1, 2, 3, 4, 5, 6, 'muchos', 'elementos']

#con delet tambien se elimina elementos pero no se recomienda
del lista1[-1]
print(lista1) #[1, 2, 3, 4, 5, 6, 'muchos']

#eliminar un rango de elementos
del lista1[1:3] #[1, 4, 5, 6, 'muchos']
del lista1[:2] #[5, 6, 'muchos']
print(lista1)

#eliminar todos los elementos de la lista
#lista1.clear()
#print(lista1) #[]

#SHORT PARA ORDENAR MODIFICANDO LA ORIGINAL "no devuelve la lista"
num = [1,11,22,5,105,55,77]
#devolver_lista = num.sort() #None NO devuelve la lista
num.sort() #[1, 5, 11, 22, 55, 77, 105] SOLO MODIFICA LA LISTA ORIGINAL
print(num)


#SHORTED CREANDO UNA NUEVA LISTA "cdevuelve una copia"
num1 = [1,11,22,5,105,55,77]
devolver_lista = sorted(num1)
print(devolver_lista) #[1, 5, 11, 22, 55, 77, 105]
print(num1) #[1, 11, 22, 5, 105, 55, 77]

#ordenar una lista de cadena de texto
frutas = ["pera", "manzana", "frutilla", "uva", "naranja"]
ord_frutas = sorted(frutas) #['frutilla', 'manzana', 'naranja', 'pera', 'uva']
print(ord_frutas)

frutas_mayus = ["pera", "manzana", "frutilla", "Uva", "Naranja"]
ord_frutas_mayus = sorted(frutas_mayus) #['Naranja', 'Uva', 'frutilla', 'manzana', 'pera'] ordena primero las mayusculas y luego las minus
print(ord_frutas_mayus)

#para ordenas una cadena de texto con mayus y minus
frutas_mayus_sort = ["pera", "manzana", "frutilla", "Uva", "Naranja"]
frutas_mayus_sort.sort(key=str.lower)
print(frutas_mayus_sort) #['frutilla', 'manzana', 'Naranja', 'pera', 'Uva']

# METODO utilies
animales = ["leon", "elefante", "puma", "leon", "llena", "cocodrilo"]
print(len(animales)) #-> 6
print(animales.count("leon")) #-> 2 
print("cocodrilo" in animales) #True comprueba si hay un "cocodrilo" en la lista    