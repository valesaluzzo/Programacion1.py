'''Identifique si un número N ingresado es primo o no'''

n = int(input("Ingrese un numero: "))
if n <= 1:
    print("No es primo")
else:
    primo = True
    
    for i in range (2, n):
        if n % i == 0:
            primo = False
    if primo:
        print("Es primo")
    else:
        print("No es primo")