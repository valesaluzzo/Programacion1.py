'''Una nueva feria llega a la ciudad. Los precios varían según la edad:
Menores de 4 años pasan gratis
Menores de 12 pagan 1/3 de tarifa
Menores de 18 pagan media tarifa
Adultos hasta 60 años pagan tarifa completa
Adultos mayores y jubilados pagan media tarifa.
Realice un programa donde se ingrese la edad de la persona y como salida indique el monto anteponiendo el signo $ y un espacio. Ejemplo para un adulto: $ 150.0'''

edad = int(input())
tarifa = 150.0
if edad < 4:
    monto = 0.0
elif edad < 12:
    monto = tarifa / 3
elif edad < 18:
    monto = tarifa / 2
elif edad < 60:
    monto = tarifa
else:
    monto = tarifa / 2

print("$", monto)