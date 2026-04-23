'''Repetición de Frase: Pide al usuario que ingrese una palabra y luego imprime esa palabra dos veces, en la misma línea y separadas por una barra diagonal "/".
La entrada es solo una palabra, y la salida es únicamente esa misma palabra escrita dos veces, pero separadas por un "/".
Ejemplo: para la entrada "clase" la salida será "clase/clase"'''

palabra = input("Ingrese una palabra: ")
print(palabra, end="/")
print(palabra)