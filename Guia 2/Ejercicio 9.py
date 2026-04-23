'''Tres personas deciden invertir su dinero para formar una empresa. Cada una de ellas invierte una cantidad distinta. 
Calcular y mostrar el porcentaje que cada una invierte con respecto al total de la inversión.'''

inversion1 = float(input("Ingresar primer inversion: "))
inversion2 = float(input("Ingresar segunda inversion: "))
inversion3 = float(input("Ingresar tercera inversion: "))

totalInversion = inversion1 + inversion2 + inversion3
porcentaje1 = (inversion1/totalInversion) * 100
porcentaje2 = (inversion2/totalInversion) * 100
porcentaje3 = (inversion3/totalInversion) * 100

print("El primer porcentaje es : ",porcentaje1, "%")
print("El segundo porcentaje es : ",porcentaje2, "%")
print("El tercer porcentaje es : ",porcentaje3, "%")