# Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado

#Silenciosa = 1920 - 1940 baby boomer = 1946 1964 generacion X = 1965 - 1979 Generación Y = 1980-2000 generación Z 2001 - 2010
año_de_nacimiento = int(input("Ingrese su año de nacimiento: "))

if año_de_nacimiento >= 1920 and año_de_nacimiento <= 1940:
    print("Sos de la generación Silenciosa")
elif año_de_nacimiento <= 1964:
    print("Sos de la generación Baby Boomer")
elif año_de_nacimiento <= 1979:
    print("Sos de la generación X")
elif año_de_nacimiento <= 2000:
    print("Sos de la generación Y")
elif año_de_nacimiento <= 2010:
    print("Sos de la generación Z")
else:
    print("No perteneces a ninguna generación")