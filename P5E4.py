# Practica 5
#   Ejercicio 4
#       Escribe un programa que pida un número y calcule su factorial.
#
#
#------------------------imports
import sys
#
#------------------------variables
numeroCuenta = 1
numeroCuentaMostrar = ""
#
#------------------------inputs
#numUno
numUno = input ("Introduce un numero :")
#
#comprobacion de numUno
try:
    numUno = int(numUno)
except ValueError:
    print ("El valor introducido no procede")
    sys.exit()
#
if numUno == 0:
    print ("El factorial de 0 es 1")
    sys.exit()
elif numUno < 0:
    print("No se puede calcular el valor factorial de un numero negativo")
    sys.exit()
elif numUno > 99999:
    print ("Demasiado grande, mi ordenador ya ha sufrido bastante probando," +\
        " el tuyo mejor que no sufra")
    arriesgarCierre = input("Introduce [procede] para calcular : ")
    if not arriesgarCierre == "procede":
        print("Abortando . . . ")
        sys.exit()
#
#
#----------------------logic
for numeroIntermedio in range (1,numUno + 1):
    numeroCuenta *= numeroIntermedio
    if numeroIntermedio == numUno:
        print ("El factorial de " + str(numUno) + " es " + str(numeroCuenta) )
        numeroCuentaMostrar += str(numeroIntermedio)
        print (numeroCuentaMostrar + " = " + str(numeroCuenta))

    else:
        numeroCuentaMostrar += str(numeroIntermedio) + " * "
