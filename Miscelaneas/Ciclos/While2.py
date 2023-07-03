 # Determinar si un numero es o no es primo.
i=0
cont=0
num = int(input("Escriba un numero mayor que cero: "))
while num <=0:
    num = int(input("Escriba un numero valido: "))
while num > 1:
    i+=1                    #aumenta para comprobar los valores desde 1 hasta num
    if num % i==0:
        cont+=1             #aumenta cada vez que i sea divisor de num 
        
    if num == i:
        if cont == 2:  
            print(f"El numero {num} es primo")
        else:
            print(f"El numero {num} no es primo")
        break
