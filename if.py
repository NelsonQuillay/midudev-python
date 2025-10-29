
import os
os.system("clear")

'''edad = 15
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")'''

'''calificacion = 9

if calificacion >=9:
    print("sobresaliente")
elif calificacion >=7:
    print("notable")
elif calificacion >=4:
    print("aprobado")
else:
    print("reprobado")'''

# Condiciones multiples

edad = 10
licencia = False


#javascript
#&& -> and
if edad >= 18 and licencia:
    print("permiso aprobado")
else:
    print("rechazado")

#|| -> or
if edad >= 18 or licencia:
    print("permiso aprobado en el pueblo")
else:
    print("rechazado en el pueblo")


#! -> not
finde = True
if not finde:
    print("trabajar a full")
else:
    print("mereces un descanso")

edad = 15
tiene_dinero = True

#! no se recomienda anidar condiciones
if edad >=18:
    if tiene_dinero:
        print("puedes entrar a la disco")
    else:
        print("no puedes entrar a la disco")
else:
    print("vete a hacer una pijamada a tu casa") 

#sintaxis mas facil
if edad < 18:
    print("no puedes entrar a la disco")
elif tiene_dinero:
    print("puedes entrar a la disco")
else:
    print("vete a hacer una pijamada a tu casa") 

# condicion ternaria
# codigo si cumple con la condicion - if condicion - else codigo si no cumple
edad = 19
repuesta = "Es mayor de edad" if edad >= 18 else "Es menor"
print(repuesta) 

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)