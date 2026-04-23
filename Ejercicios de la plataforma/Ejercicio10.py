'''Lucía, una niña de 8 años quiere comprarse un peluche que cuesta un determinado monto. Sin embargo, Lucía no sabe cuántos billetes necesita llevar a la tienda para pagar su peluche. Tiene billetes de $100, $50, $20, $10, $5 y $1.
Se necesita crear un algoritmo que, solo utilizando lo aprendido hasta el momento, le diga cuántos billetes de cada denominación necesita. Así, Lucía podrá ir a la tienda con la seguridad de que tiene el monto exacto en billetes, listo 
para comprar su peluche favorito
Entrada:
Hola Lu, ingresa el precio del peluche: $ 237
Salida:
2 billetes de $100
0 billetes de $ 50
1 billetes de $ 20
1 billetes de $ 10
1 billetes de $ 5
2 billetes de $ 1'''

print("Hola Lu, ingresa el precio del peluche: $ ", end="")
precio = int(input())

billetes_100 = precio // 100
precio = precio % 100

billetes_50 = precio // 50
precio = precio % 50

billetes_20 = precio // 20
precio = precio % 20

billetes_10 = precio // 10
precio = precio % 10

billetes_5 = precio // 5
precio = precio % 5

billetes_1 = precio // 1

print(billetes_100, "billetes de $100")
print(billetes_50, "billetes de $ 50")
print(billetes_20, "billetes de $ 20")
print(billetes_10, "billetes de $ 10")
print(billetes_5, "billetes de $ 5")
print(billetes_1, "billetes de $ 1")