'''Calcular el máximo de números positivos introducidos por
teclado, sabiendo que metemos números hasta que
introduzcamos uno negativo. El negativo no cuenta.'''

numero = int(input("Introdusca un numero positivo: "))
numeromax = 0
while numero >= 0:
    if numero > numeromax:
        numeromax = numero
    numero = int(input("Introduca un numero positivo: "))
    if numero < 0:
        print("Fin del bucle")
        break

print(f"{numeromax} es el maximo")