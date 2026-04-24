N = int(input("Ingrese la cantidad de productos: "))

if N % 100 == 0:
    resultado = N
else:
    resultado = N + (100 - (N % 100))
print("La próxima centena es:", resultado)