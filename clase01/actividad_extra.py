# Crear un programa que calcule la nota final de estudiantes del curso de Python. La nota final se calcula basandonos en tres notas previas de las cuales, 
# cada una corresponde a un porcentaje distinto de la nota final. Los porcentajes son:
# Nota_1 cuenta como el 20% de la nota final, nota_2 cuenta como el 30% de la nota final, nota_3 cuenta como el 50% de la nota final

# A tener en cuenta: El promedio entre 3 y 10 : (13.3 + 2.10)/15 el peso de 3 es 13, el peso de 10 es 2, todo esto dividido el total. 

#Entrada de datos
nota_1 =   int(input("Ingresa la nota del parcial 1: "))
nota_2 = int(input("Ingresa la nota del parcial 2: "))
nota_3 = int(input("Ingresa la nota del parcial 3: "))

#Calculo de datos
promedio = (20*nota_1 + 30*nota_2 + 50*nota_3)/100

#Salida de datos
print("El promedio del alumno es de: ", promedio)