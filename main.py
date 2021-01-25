# Este es el juego de adivinar el número.

import random

nombre = input("Introduce tu nombre\n")

numero = int(input("Introduce un numero del 1 hasta infinito\n"))
while numero < 0:
    numero = int(input("Introduce un numero positivo mamon\n"))

numero_aleatorio = random.randint(1, numero)

numero_intentado = 0

print("Intenta adivinar el numero que se ha generado entre el 1 y el " + str(
    numero) + " . Si quieres salir escribe " + str(numero + 1) + "\n")
while numero_intentado != numero_aleatorio + 1:
    numero_intentado = int(input("Adivina el numero\n"))
    if numero_intentado == numero + 1:
        print("BUUUU eres un cacas")
        break

    if numero_intentado> numero + 1:
        print("Introduce un numero entre los rangos MAMON")

    if numero_intentado > numero_aleatorio:
        print("Te has pasado")
    if numero_intentado < numero_aleatorio:
        print("Te has quedado corto")

    if numero_intentado == numero_aleatorio:
        numero_intentado == numero_aleatorio
        print("Oleeeeeeeee,", nombre + "!!!",  "ERE UN PITOLERO", "El numero es: " + str(numero_aleatorio))
        break
