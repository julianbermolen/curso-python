#Ejemplo con AND: 

a = 195
b = 30
c = 400
if a > b and c > a:
    print("Ambas son verdaderas")

# Ejemplo con OR
a = 195
b = 50
c = 500
if a > b or a > c:
    print("Una de las condiciones es verdadera")

# Ejemplo utilizando ELSE

numero = 25
if numero > 35:
    print("Alto")
else:
    print("Bajo")

# Multiples IF
x = 25
if x > 10:
    print("por encima de 10, ")
    if x>20:
        print("y también por encima de 20!")
    else:
        print("pero no por encima de 20")

# Sentencia ELIF
a = 2 + 3
if a ==4:
    print("a es igual a cuatro")
elif a ==5:
    print("a es igual a cinco")
else:
    print("no se cumple la condicion")