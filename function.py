#bloques de codigo reutilizables y parametrizables para hacer tareas especificas

from os import system
if system("clear") != 0: system("cls")

# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

# """

#funcion para imprimir algo en consola
def saludar():
    print("Hola Halloween")

'''saludar()
saludar()
saludar()
saludar()'''

#funcion con parametro
def saludar_a(nombre): #<- Parametro "nombre" es lo que acepta la funcion
    print(f"Hola {nombre}.!")

'''saludar_a("Nelson")#<- Argumento "Nelson" es lo que se le pasa a la funcion
saludar_a("Melina")
saludar_a("Maximo")
saludar_a("Alvaro")'''

#funcion con mas parametros
def sumar(a, b):
    suma = a + b
    return suma

#print(sumar(2,2))

#result = sumar(-5,3)
#print(result)

#documentar las funciones con docstring
def resta (a, b):
    '''resta dos numeros y devuelve el resultado''' #docstring
    """info de la funcione""" #docstring
    return a - b 

#print(resta.__doc__) #resta dos numeros y devuelve el resultado

#help(resta)
#Help on function resta in module __main__:

#resta(a, b)
    #resta dos numeros y devuelve el resultado


#PARAMETROS POR DEFECTO EN FUNCIONES
def multipicar (a, b = 3):
    return a * b

print(multipicar(2)) #6
print(multipicar(2, 4)) #8 

#ARGUMENTO POR POSICION Y CLAVE
def describir_persona(nombre, edad, sexo):
    print(f'Soy {nombre}, tengo {edad} años y soy {sexo}')

describir_persona("nelson", 37, "masculino") #Soy nelson, tengo 37 años y soy masculino

describir_persona(37, "masculino", "nelson") #Soy 37, tengo masculino años y soy nelson

describir_persona(edad=37, sexo="masculino", nombre="nelson") #Soy nelson, tengo 37 años y soy masculino



#argumento longitud de variables (*args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1,2,3,4,5,6,7,8,9)) #45

print("\n")

#ARGUMENTO CLAVE-VALOR VARIABLE (**kwargs) key word arguments
def mostrar_informacion (**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

mostrar_informacion(name = "nelson", edad = 25, sexo = "M")
print("\n")
mostrar_informacion(apellido = "quillay", ciudad = "SL", cp = 5700)
print("\n")
mostrar_informacion(correo = "nmq@hotmail.com", name = "Mario")
