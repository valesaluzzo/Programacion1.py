'''
•Pida la edad de una persona y la cantidad de dosis aplicadas (0, 1 o 2) 
•	Determine si es menor de edad (<18) o mayor de edad 
•	Clasifique el estado de vacunación: 
    o	Completo: 2 dosis 
    o	Parcial: 1 dosis 
    o	Sin vacunar: 0 dosis 
•	Determine acciones: 
    o	Si es menor de edad y tiene 2 dosis: "Apto para actividades escolares" 
    o	Si es mayor de edad y tiene 2 dosis: "Pase sanitario habilitado" 
    o	Si tiene menos de 2 dosis: "Debe completar esquema" 
'''

edad = int(input("Ingrese su edad: "))
dosis = int(input("Ingrese cantidad de dosis aplicadas: "))

if edad >= 18 and dosis >= 2:
    print("Estado: Completo")
    print("Pase sanitario habilitado")
elif edad < 18 and dosis >=2:
    print("Estado: Completo")
    print("Apto para actividades escolares")
elif dosis <2:
    print("Estado: Parcial")
    print("Debe completar esquema")
else:
    print("Estado: Sin vacunar")
    