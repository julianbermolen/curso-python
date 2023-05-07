#Dadas dos listas, debes realizar las siguientes tareas: 
# Añadir a la lista 1 el int 456789 y luego el str "Hola Mundo"
# Añade a la lista 2 el str "Hola y Adiós" y luego el int 5555
# Genera una lista_3 con todos los elementos de la lista 1 sin considrar el ultimo elemento
# Genera una lista 4 con todos los elementos de la lista 2 menos el primero y el ultimo.
# Finalmente genera una lista 5 con los elementos de la lista 4 y 3

lista_1 = [100,90,80,70]
lista_1.append(456789)
lista_1.append("Hola mundo")
print(lista_1)
lista_2 = [50,40,30,20]
lista_2.append("Hola y adios")
lista_2.append(5555)
print(lista_2)
#lista_1.pop()
lista_3 = lista_1[:-1] #Todos los elementos, menos el ultimo. Pop te devuelve el valor eliminado
print(lista_3)
#lista_2.pop(0)
#lista_2.pop()
lista_4 = lista_2[1:-1] # Nos salteamos el primero y el ultimo
print(lista_4)
lista_5 = lista_4 + lista_3
print(lista_5)
