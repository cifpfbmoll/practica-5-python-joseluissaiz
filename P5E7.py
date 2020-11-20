# Practica 5
#   Ejercicio 6
#       Escribe un programa que pida la altura de un triángulo y lo dibuje de la 
#       siguiente manera:
#
#
#
#------------------------imports
import sys
#
#------------------------variables
anchura = 0
numeroCuentaMostrar = ""
#
#------------------------inputs
#altura
altura = input ("Introduce la altura del triangulo :")
#
#comprobacion altura
try:
    altura = int(altura)
except ValueError:
    print ("El valor introducido no procede")
    sys.exit()
#
if altura <= 0:
    print ("Por favor, introduce un nuemro positivo")
    sys.exit()
#
#
#--------------------logic
anchura = altura
print("\n")
print("Este es tu triangulo bonito")
print("\n")
for numeroIntermedio in range(altura):
    anchura -= 1
    for numeroIntermedio in range(anchura):
        print("  *  ", end='')
    print("\n")