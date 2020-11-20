#Practica 5
#   Ejercicio 9
#       Escribe un programa que pida la anchura y la altura de un 
#       rectángulo y lo dibuje de la siguiente manera:
#
#--------Imports
import sys
#--------Inputs
anchura = input("Escribe la anchura del rectangulo : ")
altura = input("Escribe la altura del rectangulo : ")
#
#comprobaciones
try:
    anchura = int(anchura)
    altura = int(altura)
except ValueError:
    print ("Valor no valido")
    sys.exit()
#
#--------Menu
print("")
print("")
print("ESTE ES TU RECTANGULO BONITO")
print("")
#--------Logic
for numeroIntermedio in range(altura):
    if numeroIntermedio == 0 or numeroIntermedio == altura - 1:
        for numeroIntermedio in range(anchura):
            print ("  *  ",end='')
        print("")
        print("")        
    else:
        for numeroIntermedio in range(anchura):
            if numeroIntermedio == 0 or numeroIntermedio == anchura - 1:
                print("  *  ",end='')
            else:
                print("     ",end='')
        print("")
        print("")