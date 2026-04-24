'''
•	Pida la edad de un alumno y su porcentaje de asistencia (0 a 100) 
•	Determine si es menor de edad o mayor de edad 
•	Clasifique la asistencia: 
    o	Excelente: >= 90 
    o	Buena: >= 75 
    o	Regular: >= 60 
    o	Baja: < 60 
•	Determine condición: 
    o	Si es menor de edad y asistencia >= 75: "Regulariza la materia" 
    o	Si es mayor de edad y asistencia >= 90: "Promoción directa" 
    o	Si asistencia < 60: "Libre por inasistencias" 
'''
edad = int(input("Ingrese su edad: "))
asistencia = float(input("Ingrese el porcentaje de sus asistencias: "))

if edad >= 18 and asistencia >= 90:
    print("Es mayor de edad")
    print("Asistencia: Excelente")
    print("Promoción directa")
elif edad < 18 and asistencia  >= 75:
    print("Es menor de edad" )
    print("Asistencia: Buena")
    print("Regulariza la materia" )
elif asistencia >= 60:
    print("Asistencia: Regular")
else:
    print("Asistencia: Baja")
    print("Libre por inasistencias")
    