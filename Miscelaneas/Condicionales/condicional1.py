#Pedir 3 numeros e indicar cual de ellos es el valor del medio.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 < num2 < num3 or num3 < num2 < num1:
    print ("El numero medio es ", num2)

elif num2 < num1 < num3 or num3 < num1 < num2:
    print ("El numero medio es ", num1)

else:
    print ("E numero medio es ", num3)

