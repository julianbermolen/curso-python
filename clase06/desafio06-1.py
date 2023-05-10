"""
Tenemos dos listas de numeros

lista_1 = [1,2,3,4,5]
lista_2 = [3,4,5,6,7]

Encontrar los numeros que aparecen en ambas listas sin duplicados. Usando conjuntos para realizar esta operacion de manera eficiente
"""

lista_1 = [1,2,3,4,5]
lista_2 = [3,4,5,6,7]

conjunto_1 = set(lista_1)
conjunto_2 = set(lista_2)

conjunto_duplicados = conjunto_1.intersection(conjunto_2)

print(conjunto_duplicados)

