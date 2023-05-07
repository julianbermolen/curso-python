"""
Un curso se dividio en 2 grupos: A y B de acuerdo al nombre y a una preferencia (marvel o capcom)
El grupo A esta formado por: Fans de marvel y la letra inicial anterior a la "M" fans de capcon y letra inicial de nombre posterior a la "C"
El grupo B por el Resto.
Imprimir por pantalla piidendole el nombre y respondiendo a que grupo pertenece
"""

# Entrada de datos
nombre = input("Ingrese su nombre: ")
preferencia = input("Ingrese su preferencia Marvel o Capcom?: ")

# Operaciones
condicion_a = preferencia=="Marvel" and nombre[0]<"m"
condicion_b = preferencia=="Capcom" and nombre[0]>"c"

if condicion_a:
    grupo = "Pertenece al grupo A"
elif condicion_b:
    grupo = "Pertenece al grupo A"
else: 
    grupo = "Pertenece al grupo B"

# Salida de datos
print(grupo)