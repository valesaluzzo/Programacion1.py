'''Datos Personales: Escribe un programa que imprima en la consola los datos personales de una persona.
Las entradas deben ser:
Ciudad de residencia
DNI
Nombre completo
La salida debe ser:
{dni} - {ciudad} - {nombre}
Ejemplo:
Para los datos Villa Maria, 12345678, Juan Perez, la salida debe ser "12345678 - Villa Maria - Juan Perez"'''

ciudad = input("Ingrese su ciudad: ")
dni = input("Ingrese su DNI: ")
nombre = input("Ingrese su nombre: ")

print(dni, "-",ciudad,"-",nombre)