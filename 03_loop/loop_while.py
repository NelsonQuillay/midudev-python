#! WHILE
#! Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición

#bucle con simple condicion

'''
cont = 0

while cont <5:
    print(cont)
    cont += 1
    print(cont)'''


#bucle con break

'''
cont = 0

while True:
    print(cont)
    cont +=1
    if cont == 5:
        break'''

#bucle con continue

'''
cont = 0

while cont < 10:
    cont += 1

    if cont %2 == 0:
        continue # vuelve a la iteracion. todo el codigo debajo de continue no se ejecuta.

    print(cont)'''

#bucle con else

'''cont = 0'''

'''while cont <=10:
    print(cont)
    cont +=1

else:
    print("Termino el bucle")'''

'''while cont <=10:
    print(cont)
    cont +=1
    break'''

#print("Termino el bucle") #aca se ejecuta luego del break

'''else:
    print("Termino el bucle")''' #aca no se ejecuta luego del break, entonces me indica que todavia no termina de verificar todos los casos hasta encontrar una condicion de salida.



#ejercicio practico
#pedir al usuario que ingrese numero positivo

'''num = -1

while num <= 0:

    num = int(input("Ingrese un numero positivo: "))
    if num <= 0:
        print("El numero debe ser positivo, intenta otra vez")

print(f"El numero introducido es positivo: {num}")

'''

num = -1

while num <= 0:
    try:
        num = int(input("Ingrese un numero positivo: "))
        if num <= 0:
            print("El numero debe ser positivo, intenta otra vez")
    except:
        print("favor de ingresar un numero")

print(f"El numero introducido es positivo: {num}")


###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

