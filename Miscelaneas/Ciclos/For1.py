'''Determinar si un número es o no es perfecto. Un numero es
perfecto si la suma de sus divisores sin incluir el propio
número es igual a este'''

numero = int (input("Ingrese un numero: "))
suma = 0

for i in range (1,numero + 1): 
    if numero %  i ==0:
        print("El numero ", i , "es divisor de",numero   )
        suma+=i
        
resta = suma -numero
if resta == numero:
    print(f"El numero {numero} es perfecto.") 
else:
    print(f"El numero {numero} no es perfecto.")