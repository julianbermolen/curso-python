# A partir de dosvariables Nombre y Edad debes crear una variable que almacene si se complen todas las siguientes condiciones
# mostrar al usuario True or False

#nombre sea diferente de cuatro asteriscos ****
#edad sea mayor que 5 y a su vez menor que 20
#que la longitud del nombre sea mayor o igual a 4 pero a la vez menor que 8
#edad multiplicada por 3 sea mayor que 35

#Entrada de datos
nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))

#Operaciones
validar_nombre = nombre != "****"
validar_edad = edad>5 and edad<20 and edad*3>35
validar_long_nombre = len(nombre)>=4 and len(nombre)<8

#Salida de datos
print(nombre)
print(validar_nombre and validar_edad and validar_long_nombre)