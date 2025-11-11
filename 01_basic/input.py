#print("hola, como te llamas?")
#nombre = input()

#nombre = input("hola, como te llamas? ")
nombre = input("hola, como te llamas?\n")

print(f"hola {nombre}, encantado en conocerte!")

age = input("cuantos años tienes?\n")
print(f"Dentro de 20 años tendras {int(age) + 20}")

print("Obtener multiples valores a la vez")
country, city = input("en que pais y cuidad vives?\n").split()

print(f"Vives en {country}, {city}")