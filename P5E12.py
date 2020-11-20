#Practica 5
#   Ejercicio 12
#       Escribe un programa que pida un número y escriba si primo o no
#
#-------Imports
import sys
#
#-------Variables
numeroPrimo = True
numeroDivision = 1
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
    if numero % numeroDivision == 0 and numeroDivision != 1 \
        and numero != numeroDivision :
            
        numeroPrimo = False
    numeroDivision += 1





if numeroPrimo == False:
    print("El numero no es primo")
else:
    print("El numero es primo")