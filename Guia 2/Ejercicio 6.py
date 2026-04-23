'''Se tiene como datos los sueldos de tres empleados: Suel1, Suel2, Suel3 y tres descuentos variables 
expresados como porcentajes: Porc1, Porc2, Porc3, respectivamente. Calcular y mostrar cada uno de los sueldos netos.'''

suel1 = float(input("Ingresar sueldo 1: "))
suel2 = float(input("Ingresar sueldo 2: "))
suel3 = float(input("Ingresar sueldo 3: "))

porc1 = float(input("Ingresar descuento 1: "))
porc2 = float(input("Ingresar descuento 2: "))
porc3 = float(input("Ingresar descuento 3: "))
#Calculo sueldos netos
neto1 = suel1 - ((suel1 * porc1)/100)
neto2 = suel2 - ((suel2 * porc2)/100)
neto3 = suel3 - ((suel3 * porc3)/100)

print("El sueldo neto 1 es de: $",neto1)
print("El sueldo neto 2 es de: $",neto2)
print("El sueldo neto 3 es de: $",neto3)
