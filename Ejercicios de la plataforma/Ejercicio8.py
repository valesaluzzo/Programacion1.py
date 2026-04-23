'''Con tu grupo de amigos salen muy seguido a comer a distintos 
bares y restaurantes de la ciudad. Dividir la cuenta es un problema, ya que el 
importe es grande y la cantidad de amigos siempre varía en cada salida. Haz un programa que resuelva el 
problema, donde la primera entrada sea la cantidad de amigos, la segunda entrada sea el total de la cuenta 
(sin símbolo de $, y con valores decimales).
La salida debe ser:
El total que debe pagar cada uno es de: ${monto}'''

amigos = int(input("Ingrese la cantidad de amigos: "))
cuenta = float(input("Ingrese el total de la cuenta: "))
total= cuenta / amigos
print("El total que debe pagar cada uno es de: $",total)