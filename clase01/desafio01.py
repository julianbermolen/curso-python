#Jugaron 20 partidos durante el torneo
#Los partidos tienen distintos puntajes 3 G 1 E 0 P
# El promedio resulta de cantidad de punto total divididos cantidad de partidos

#Declaración de variables Constantes pueden cambi

PUNTOS_PARTIDO_GANADO = 3
PUNTOS_PARTIDO_EMPATADO = 1
PUNTOS_PARTIDO_PERDIDO = 0
PARTIDOS_JUGADOS = 20

# Entrada de datos
cantidad_ganados = int(input("Cantidad de partidos ganados: "))
cantidad_empatados = int(input("Cantidad de partidos empatados: "))
cantidad_perdidos = int(input("Cantidd de partidos perdidos: "))

# Operación
puntaje_total = ((cantidad_ganados * PUNTOS_PARTIDO_GANADO)+(cantidad_empatados * PUNTOS_PARTIDO_EMPATADO))

promedio=(puntaje_total / PARTIDOS_JUGADOS)

# Salidas 
print("El promedio es de: ", promedio)