'''
•	Pida la edad del cliente y el monto total de compra 
•	Determine si es menor de edad o mayor de edad 
•	Clasifique el tipo de compra: 
    o	Alta: >= 10000 
    o	Media: >= 5000 
    o	Baja: < 5000 
•	Aplique beneficios: 
    o	Si es mayor de edad y compra >= 10000: "Descuento del 15%" 
    o	Si es menor de edad y compra >= 5000: "Descuento del 10%" 
    o	Si compra < 5000: "Sin descuento" 
'''
edad = int(input("Ingrese su edad: "))
total = float(input("Ingrese el total de su compra: "))

if edad >=18 and total >= 10000:
    print("Tipo de compra: Alta")
    print("Descuento del 15%")
elif edad <18 and total >=5000:
    print("Tipo de compra: Media")
    print("Descuento del 10%")
elif total < 5000:
    print("Tipo de compra: Baja")
    print("Sin descuento")