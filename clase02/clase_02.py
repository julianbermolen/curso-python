# Imprimimos una lista con distintos tipos de datos
# mi_lista = ["cadena", 1000, 12.34]
# print(mi_lista)
mi_variable = 1000
mi_lista = ["cadena", mi_variable, 12.34, "cadena"]
mi_lista.append("me agregué")
mi_lista.append(1+2+3)
mi_lista.pop()
print(mi_lista.index("cadena"))
print(mi_lista.count("cadena"))
print(mi_lista)


datos = [155, [2, 3, 4], "Una cadena", "Otra cadena"]
otros_datos = (2, (5, 7, 8), 1, 8)
lista_con_tupla = [1, (2, 3, 4), "Una cadena", "Otra cadena"]
tupla_con_lista = (2, [5, 7, 8], 1, 8)