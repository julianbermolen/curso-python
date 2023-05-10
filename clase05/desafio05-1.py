"""
Calcular la suma de una cantidad de números enteros ingresados por el usuario directamente utilizando la función input()
Para finalizar la ejecución, el usuario debe escribir la palabra exit. El programa debe validar dicha acción.
Finalmente, debe mostrar la suma parcial y total obtenida
"""

continuar = True # Bandera
numero = 0 # Acumulador 

while continuar:
    entrada=input("Qué número deseas sumar? Si quieres salir, escribe exit")
    if entrada == "exit":
        continuar = False
    else:
        entrada=int(entrada)
        numero+= entrada
    print("Suma Parcial: ", numero)

print("El total es de: ",numero)