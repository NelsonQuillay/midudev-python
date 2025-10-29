my_name = "nelson"
#print(my_name)

#age = 25
#print(age)

age = 37
#print(age) #se puede reasignar los valores

# tipado dinamico
# el tipo de datos se determina  en tiempo de ejecucion

name = "nelson"
print(type(name)) #str

name = 37
print(type(name)) #int

# tipado fuerte = python no realiza conversiones de tipo automatico
#print(10 + "2") #error
# en javascript si lo hace automaticamente por que es de tipado debil


#f-string (literal de cadena de formato)
print(f'hola {my_name}, tengo {age} años') #hola nelson, tengo 37 a�os


#no se recomienda asignar varias variables en una linea, pero si se puede
name, age, city = "mario", 20, "san luis" 


#convencion de nombre de variables
mi_nombre_de_variable = "ok" #snake_case el recomendado

#javascript
#const edad = 10

#python
MI_CONSTANTE = 3.14 #UPPER_CASE para indicar que se deberia dejar como constante esta variable

is_user_logged_in: bool = True #indical el type es como una anotacion o comentario type annotation
print(is_user_logged_in) 
is_user_logged_in = 123
print(is_user_logged_in)
# pero python no revisa los tipos, pero en la conf. del editor en typecheck podes aditar el modo, que por defecto esta en off

###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")