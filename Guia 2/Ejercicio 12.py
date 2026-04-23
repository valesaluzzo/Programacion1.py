'''Teniendo como dato un número par N, calcular y mostrar los cinco impares siguientes a él.'''

N = int(input("Ingresar un nuemero par: "))

for i in range(5):
    impar = N + 1 + (2 * i)
    print("Los 5 impares son: ",impar)