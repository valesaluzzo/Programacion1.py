'''Sean N y M dos números naturales, escriba un algoritmo para determinar si N es divisible por M'''

print("N y M son numeros naturales")
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))
if M != 0:  #si M es distinto a 0
    if N % M == 0:  #Calcula el resto de dividir N por M
        resultado = N / M
        print("N es divisible por M y el resultado es: ", resultado)
    else:
        print("N NO es divisible por M")
else:
    print("No se puede dividir por cero")