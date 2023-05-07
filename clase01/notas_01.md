Clase 1 - Cadenas de textos y Números


Definiciones

- Phyton es sensible a las mayusculas y a la identación (No permite espacios al principio del codigo)
- Para ejecutar un archivo en terminal, se deberá situar en el directorio donde se encuentre el archivo y escribir: python clase_01.py en consola.

Tipos de número en python

Enteros, Números de punto flotante y números complejos.
Operadores:
SUma + 
resta - 
multiplicacion * 
potencia ** 
division / 
division (Parte entera) // 
division(resto) %


Cadenas de texto en phyton 


"esto es un 'texto' entre comillas dobles"
'esto es un texto entre comillas simples'
"esto es un \"texto"\ entre comillas simples"
para que no tome los caracteres especiles, se coloca una r antes del " -> print(r"c:/hola")
Para imprimir una cadena en varias lineas: """ HOLA
que tal
 """

Código

print("hola"); --> Asi se imprime en la terminal
input("Ingrese algo"); --> Asi se pide el ingreso de datos en terminal.
int(input("ingrese algo")); --> De este modo, nos aseguramos que lo que se ingresa sea un entero.
len(frase) -> Devuelve la longitud de la cadena.
str(10) -> Transforma en cadena un entero
Slicing (Rebanar)
Frase = "Hola, como estas?"
mi_slice = Frase [0 : 3]
print(mi_slice) -> "Hol"

Variables en programación

Son datos que pueden cambiar su valor dentro de un sistema. En ellos, se puede guardar información. En phyton, son objetos.
1 - Tienen un identificador unico. Se puede ver id(a) te devolverá el identificador del objeto a creado anteriormente. Si se da el valor de a a otra variable, tendrá el mismo id ya que solo lo guarda una vez.
2 - Tiene un tipo de dato.
3 - Tienen una referencia a = 2 -> En este caso la referencia es a y tendrá de valor 2.
Las variables por convención se manejan con snake_case: fecha_de_nacimiento, las variables no pueden tener espacio en blanco.
Python es de tipado dinamico, es decir las constantes pueden cambiar aunque no es recomendable.
Longitud de cadenas Función LEN.
Indexación de strings: Cada caracter tiene una posición en la cadena.Tiene un indice. PYTHON. El indice siempre comienza en 0.
frase[0] = "P"