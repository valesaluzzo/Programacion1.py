'''Dado un número natural N, se quiere obtener un número real R que sea el resultado de
dividir la suma de los dígitos de N por la cantidad de dígitos que posee N. 
Por ejemplo: Si N = 3421 luego R = 10/4 = 2.5'''

N = int(input("Ingresar un nuemero: "))
suma = 0
cantidad = 0
while N > 0:    #sigue repitiendo mientras el número tenga dígitos
    digito = N % 10   # %10 te da el ultimo digito
    suma += digito    #suma el digito
    cantidad += 1     #cuenta el digito
    N = N // 10       # //10 elimina el ultimo digito

resultado = suma / cantidad
print("El resultado es: ",resultado)