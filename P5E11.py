#Practica 5
#   Ejercicio 11
#       Escribe un programa que pida un número e imprima todos sus 
#       divisores.
#
#-------Imports
import sys
#
#-------Variables
resultado = ""
#-------Inputs
numero = input("Dame un numero : ")
try:
    numero = int(numero)
except ValueError:
    print("Valor no valido")
    sys.exit()
#
#-------Logic
for i in range(numero):
    if i != 0:
        if numero % i == 0:
            resultado = resultado + " " + str(i)
print("Los divisores de " + str(numero) + " son" + resultado + " " \
        + str(numero))