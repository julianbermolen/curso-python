Clase 02 - Tuplas y Listas

Representación de lista es: <list>.
Son colecciones que guardan distintos elementos. Por ejemplo, lista de items separados por comas y contenidos dentro de dos corchetes.
mi_lista = [-11, 20, 3, 41]
otra_lista=["hola", "como", "estas"]
En python, no hay restricción por tipo de dato en las listas. Se pueden guardar variables en la lista:
mi_variable = "Hola"
mi_lista = ["cadena", 1000, 12.34, mi_variable]
al imprimir se verá el "Hola" reemplazando la variable

print(mi_lista[0]) --> "cadena"
print(mi_lista[-1]) --> "hola"
Los strings son inmutables, es decir, no cambian. Pero las listas si pueden mutar.
mi_lista[3] = "chau"

Funciones de listas
¿Que son? Son herramientas que las listas traen consigo, funciones integradas.
Append
Permite agregar un nuevo item al final de una lista.
mi_lista.append(ELEMENTO)
Len
Permite saber la longitud de la lista
len(mi_lista)
Pop
Elimina un elemento de la lista. El último.
pop(indice)
Count
Cuenta los elementos con el valor indicado.
Numeros = [1,2,1,3,1,4,1]
print(Numeros.count(1))
4
Index
Esta función busca un elemento y nos dice en que índice se encuentra.



Tuplas

Las tuplas  NO pueden modificarse. Son inmutables.
tupla = (1, 2, "hola") -> Lo mismo pero con parentesis.
Las tuplas no contienen la funcion append() pero se puede agregar concatenando.
tupla+=("hola", ) -> La coma al final, solo se conctena con tuplas

Anidacion 
Listas dentro de listas
datos = [155, [2, 3, 4], "Una cadena", "Otra cadena"]
otros_datos = (2, (5, 7, 8), 1, 8)
lista_con_tupla = [1, (2, 3, 4), "Una cadena", "Otra cadena"]
tupla_con_lista = (2, [5, 7, 8], 1,😎

transformación de tuplas
list(tupla) -> Igual que la funcion para transformarlo en string.