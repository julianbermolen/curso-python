numero=5
while numero > 0:
    print(numero)
    numero-=1
print("Terminé de contar")


intento = 1
while intento <= 3:
    respuesta = input("Escribe SI: ")
    if respuesta == "SI":
        print("Saliste del programa en el intento",intento)
        exit()
    intento += 1
else:
    print("Has agotado tus tres intentos")
