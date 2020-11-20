# Practica 5
#   Ejercicio 1
#       Escribe un programa que escriba a los siguientes números (la separación 
#       entre número es para facilitar cuántos números se deben escribir en cada 
#       bucle) y en el que la función range que utilices tenga un ÚNICO argumento 
#       y que el valor de este se corresponda con el número de elementos que 
#       aparecen en la lista ( por Ejemplo, para la primera lista range (10)).
#
#
#
#----------------crear listas
numMostrar = 0
for num in range(10):
    numMostrar += 1
    print(numMostrar,end=" ")


print ("")

numMostrar = 0
for num in range(10):
    numMostrar += 2
    print(numMostrar,end=" ")


print ("")


numMostrar = 18
for num in range(10):
    numMostrar += 2
    print(numMostrar,end=" ")



print ("")


numMostrar = 6
for num in range(10):
    numMostrar += 4
    if numMostrar <= 30:
        print(numMostrar,end=" ")



print ("")


numMostrar = 45
for num in range(10):
    numMostrar -= 5
    if numMostrar >= 0:
        print(numMostrar,end=" ")