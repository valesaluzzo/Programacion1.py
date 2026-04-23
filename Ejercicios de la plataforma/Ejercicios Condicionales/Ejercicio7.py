'''Utilizando la estructura condicional multiple.
Realice un algoritmo que ingresando un número del 0 al 5, muestre un mensaje indicando el mismo numero escrito en letras.
Entrada: 1
Salida: "uno"'''

n = int(input("Ingrese un numero del 0  al 5: "))
if n == 0:
    print("Cero")
elif n == 1:
    print("uno")
elif n == 2:
    print("dos")
elif n == 3:
    print("tres")
elif n == 4:
    print("cuatro")
elif n == 5:
    print("cinco")
else:
    print("Numero fuera de rango")