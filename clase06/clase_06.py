"""
Crear un conjunto en python de colores:
Que posea los siguientes elementos - Rojo, blanco y azul.
Luego agregamos violata y dorado.
Elimina los colores: Celeste, blanco y dorado.
"""

conjunto_colores = {"Rojo", "Blanco", "Azul"}
print("Conjunto de colores: ", conjunto_colores)

conjunto_colores.update({"Violeta", "Dorado"})
print("Conjunto de colores: ", conjunto_colores)

conjunto_colores.discard("Celeste")
conjunto_colores.discard("Blanco")
conjunto_colores.discard("Dorado")
print("Conjunto de colores: ", conjunto_colores)