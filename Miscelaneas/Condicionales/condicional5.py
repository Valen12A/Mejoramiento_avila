# Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número exceda los límites emita un mensaje y finalice el programa

numero = int(input("Ingrese un numero mayor que 0 y menor que 9999: "))

if numero < 0 or numero > 9999:
    print("El número está fuera de los límites.")
else:
    cifras = len(str(numero))
    print("El número tiene", cifras, "cifra.")





