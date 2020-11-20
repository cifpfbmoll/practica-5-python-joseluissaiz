# Practica 5
#   Ejercicio 3
#       Escribe un programa que pida dos números y escriba la suma de enteros 
#       desde el primero hasta el último.
#
#
#------------------------imports
import sys
#
#------------------------variables
numeroCuenta = 0
numeroCuentaMostrar =  ""
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
    numeroCuenta += numeroIntermedio
    if numeroIntermedio == numDos:
        print ("La suma desde " + str(numUno) + " hasta " + str(numDos) + \
            " es : " + str(numeroCuenta) )
        numeroCuentaMostrar += str(numeroIntermedio)
        print (numeroCuentaMostrar + " = " + str(numeroCuenta))

    else:
        numeroCuentaMostrar += str(numeroIntermedio) + " + "
