# permite crear una secuencia o rango de numeros. Se usa frecuentemente en for
# NO CREA UNA LISTA

#range(x)
#por defecto el inicio es 0 (cero)=> range(0,x) 
#por defecto el paso es 1 (uno)=> range(0, x, 1)


#crear una secuencia de numero del 0 al 9
#range (fin)
'''for num in range(10):
    print(num)'''

#crear una secuencia de numero del 3 al 9
#range (inicio, fin)
'''for num in range(3, 10):
    print(num)'''

#crear una secuencia de numero del 3 al 9 en 2
#range (inicio, fin, paso)
'''for num in range(3, 10, 2):
    print(num)'''

#uando con numeros negativos
'''for num in range(-5, 0):
    print(num)'''

'''for num in range(10, 0, -1):
    print(num)'''

#usamos list para realizar una lista 
'''nums = range(10)
list_of_nums = list(nums)
print(list_of_nums) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'''

#Ej: para hacer 5 veces algo
'''contador=0
while contador <=5:
    print("hacer 5 veces algo")
    contador +=1
'''
#con range se puede hacer mas corto
for _ in range(5): print("hacer 5 veces algo") #_ cuando no se va a utilizar esa variable   

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
