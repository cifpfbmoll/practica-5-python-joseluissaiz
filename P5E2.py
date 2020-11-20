# Practica 5
#   Ejercicio 2
#       Escribe un programa que pida dos números y escriba qué números entre ese 
#       par de números son pares y cuáles impares
#
#
#------------------------imports
import sys
#
#------------------------inputs
#numUno
numUno = input ("Introduce un numero :")
#
#comprobacion de numUno
try:
    numUno = int(numUno)
except ValueError:
    print ("El valor uno no procede")
    sys.exit()
#
#numDos
numDos = input ("Introduce otro numero mayor que " + str(numUno) + " :")
#
#comprobacion de numDos
try:
    numDos = int(numDos)
except ValueError:
    print ("El valor dos no procede")
    sys.exit()
#
#
if numDos <= numUno:
    print ("El valor introducido es inferior o igual al anterior")
    sys.exit()
#
#
#
#-----------------------logic
for numeroIntermedio in range(numUno,(numDos + 1)):
    if numeroIntermedio % 2 == 0:
        print ("El número " + str(numeroIntermedio) + " es par")
    else:
        print ("El número " + str(numeroIntermedio) + " es impar")
