#conversion de tipos

print(type("100"))

print(type(int("100")))#pasar a entero

#print(2 +"100") #Error

print(2 + (int("100"))) #102 se suma

print(str(2) + "100") #2100 se concatena

print(float("3.1416")) #de string a flotante

print(int(3.1416)) #3 elimina la parte del decimal

#redondeo
print(round(2.5)) #2 cuando el decimal es 5, el redondeo se realiza al par mas cercano
print(round(3.5)) #4

#bool con numeros
print(bool(5)) #True
print(bool(0)) #False es el unico valor que devuelve False
print(bool(-5)) #True

#bool con string
print(bool("")) #False
print(bool(" ")) #True
print(bool("False")) #True