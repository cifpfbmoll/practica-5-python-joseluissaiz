#Practica 5
#   Ejercicio 10
#       Escribe un programa que pida la altura de un triángulo y lo 
#       dibuje de la siguiente manera:
#
#--------Variables
numeroLinea = 1
#
#---------Imports
import sys
#---------Inputs
altura = input("Introduce la altura del triangulo : ")
try:
    altura = int(altura)
except ValueError:
    print ("Valor no valido")
    sys.exit()
#
espacios = altura -1
#
#--------Mostrar Menu
print("")
print("")
print("ESTE ES TU TRIANGULO BONITO")
print("")
#--------Logic
for numeroIntermedio in range(altura):
    for i in range(espacios):
        print(" ",end='')

    for i in range(numeroLinea):
        print("*",end='')
    print("")
    numeroLinea += 2
    espacios -= 1

    

            
