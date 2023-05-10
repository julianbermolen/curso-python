"""
Escribe un programa genere un número aleatorio entre 1 y 10.
Le debes pedir al usuario que log adivine en un máximo de 3 intentos. 
Si el usuario adivina el número,  deberás imprimir un mensaje de felicitación 
con el número de intentos que se tomaron para adivinarlo. 
Si el usuario no logra adivinar el número en los 3 intentos,
el programa deberá imprimir un mensaje que indique que no se logró adivinar el número. 

Para manejar números aleatorios vamos a utilizar la biblioteca random.
Y de random la función randint() que genera un número entero,
recibe como parámetros 2 números, separados por coma, el mínimo y el máximo del rango.
from random import randint
randint(x, y)
"""
from random import randint

numero_aleatorio = randint(1,10)

count = 3

while count > 0:
    numero = int(input("Adivine el número del 1 al 10: "))
    if(numero == numero_aleatorio):
        print("Felicitaciones! Ganaste! Numero random: ",numero_aleatorio)
        break
    else:
        print("Error, elija otro: ")
        count=count-1

else:
    print("No lograste adivinar, lo lamento. Número random: ", numero_aleatorio)