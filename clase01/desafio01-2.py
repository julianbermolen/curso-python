# Teniendo el siguiente string, ordenarlo para que no este al revez, para ello utilizar el siguiente comando CADENA[::-1] e imprimir los datos correspondiente por separado
cadena = "acitametam ,8 ,zepol ordeP"

cadena_real = cadena[::-1]

nombre_apellido = cadena_real[0:11]
nota = cadena_real[13:14]
materia = cadena_real[16:26]

print(nombre_apellido + " " + nota + " " + materia)