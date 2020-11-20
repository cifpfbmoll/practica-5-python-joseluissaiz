# Practica 5
#   Ejercicio 5
#       Escribe un programa que pida la altura y ancho de un rectángulo y lo 
#       dibuje de la siguiente manera:
#
#
#------------------------imports
import sys
#
#------------------------variables
numeroCuentaMostrar = ""
#
#------------------------inputs
#anchura
anchura = input ("Introduce la anchura del rectangulo :")
#
#comprobacion anchura
try:
    anchura = int(anchura)
except ValueError:
    print ("El valor introducido no procede")
    sys.exit()
#
if anchura <= 0:
    print ("Por favor, introduce un nuemro positivo")
    sys.exit()
#
#
#altura
altura = input ("Introduce la altura del rectangulo :")
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
print("\n")
print("Este es tu rectangulo bonito")
print("\n")
for numeroIntermedio in range(altura):
    for numeroIntermedio in range(anchura):
        print("  *  ", end='')
    print("\n")
