#Determinar los divisores de un número introducido por teclado

numero = int (input("Ingrese un numero: "))
i=0
while True:
    i+=1
    if numero % i ==0:                                   #Se divide numero en i si el resultado es 0 i es divisor de numero
        print(f"El numero {i} es divisor de {numero}")
        
    if numero==i:
        break