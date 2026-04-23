'''Ingresar un número entero N, calcular y mostrar la sumatoria de los 5 enteros posteriores a N.'''

N = int(input("Ingresar un nuemero: "))
suma = 0

for i in range(1, 6):  #repite el ciclo 5 veces
    suma = suma + (N + i)

print("La sumatoria es: ",suma)