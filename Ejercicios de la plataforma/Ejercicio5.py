'''Utilizando el código disponible a continuación, debes copiar y pegarlo dentro de VPL y modificarlo como creas necesario para lograr que la salida coincida con la indicada al final. No puedes agregar sentencias print ni modificar el texto escrito, solo se permite modificar la configuración de separadores (concatenación) y final en los lugares donde creas correspondiente.
Código base:
print("Hola")
print("mundo")
print("Esto es")
print("Programación 1")
print("De la carrera", "tecnicatura en programación")
print("UTN", "FRVM")
Salida esperada:
Hola mundo
Esto es >> Programación 1 <<
De la carrera: tecnicatura en programación en UTN-FRVM
Aclaraciones:
No pueden modificar los bloques de texto (lo que esté entre comillas)
No pueden agregar prints
Lo único que pueden hacer es agregar a los print existentes las configuraciones de final y separador.'''

print("Hola",end=" ")

print("mundo")

print("Esto es ", end=" >>")

print("Programación 1",end="<<")

print("\nDe la carrera", "tecnicatura en programación", end=" en ")

print("UTN", "FRVM", sep="-")