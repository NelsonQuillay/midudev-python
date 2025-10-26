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

