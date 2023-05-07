# El cliente debe ser mayor de edad. tener antiguedad en el sistema de minimo 3 años e ingreso mayor de 2500
#si su antiguedad no es suficiente su ingreso mensual debe ser 4000 como minimo
# si no se cumple, no se aprueba el credito
# Ingresar datos dos tipos, int y float, evaluar las condiciones y mostrar el resultado

# Ingreso de datos
edad = int(input("Ingrese su edad: "))
antiguedad=int(input("Ingrese su antiguedad en el sistema financiero: "))
ingresos=float(input("Ingrese sus ingresos mensuales: "))

# Procesamiento de datos

if edad>=18 and antiguedad>=3 and ingresos>=2500:
    credito="Aprobado"
elif edad>=18 and antiguedad<3 and ingresos>=4000:
    credito="Aprobado por el ingreso"
else:
    credito="No aprobado"

# Salida de datos
print(credito)