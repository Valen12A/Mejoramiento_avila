import random

tam = 5
rango = 20

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for i in lista:
        sum+=i
    return sum

def sumaMayor(lista1, lista2):
    sum1 = sum (lista1)
    sum2 = sum (lista2)
    if sum1 > sum2:
        return f"La suma mayor de las dos listas es: {sum1}"
    elif sum1 < sum2:
        return f"La suma mayor de las dos listas es: {sum2}"
    else:
        return "Las sumas son iguales"
    

def mayorLista(lista):        
    maximo = lista[0]                    
    for i in lista:
        if i > maximo:
            maximo=i
    return maximo

def mayorListas(lista1,lista2):
    num1 = mayorLista(lista1)
    num2 = mayorLista(lista2)
    for i in lista1 and lista2:
        if num1 > num2:
            return f"El numero mayor de las dos listas es: {num1}"
        elif  num2 > num1:
            return f"El numero mayor de las dos listas es: {num2}"
        else:
            return f'El numero es igual en las dos listas'

def menorLista(lista):
    minimo=lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return  minimo

def menorListas(lista1, lista2):
    num1 = menorLista(lista1)
    num2 = menorLista(lista2)
    for i in lista1 and lista2:
        if num1 < num2:
            return f"El numero menor de las dos listas es: {num1}"
        elif  num2 < num1:
            return f"El numero menor de las dos listas es: {num2}"
        else:
            return f'El numero es igual en las dos listas'
 
def promedioLista(lista):     
    return sumaLista(lista)/len(lista)



def promedioListas1(lista1, llista2):
    sumatotal= sumaLista(lista1) + sumaLista(llista2)
    tamTotal= len(lista1) + len(llista2)
    promedioTotal= sumatotal / tamTotal
    print(f"El promedio de las dos listas es: {promedioTotal}")
    
    if  promedioTotal < promedioLista(lista1):
        return 'El promedio de la primera lista esta por debajo del promedio total'
    elif promedioLista(lista1) == promedioListas1:
        return 'El promedio de la lista y el promedio total son iguales'
    else:
        promedioLista(lista1) > promedioTotal
        return 'El promedio de la primera lista esta por encima del promedio total'

def promedioListas2(lista1, llista2):
    sumatotal= sumaLista(lista1) + sumaLista(llista2)
    tamTotal= len(lista1) + len(llista2)
    promedioTotal= sumatotal / tamTotal
    print(f"El promedio de las dos listas es: {promedioTotal}")
    
    if  promedioTotal < promedioLista(lista2):
        return 'El promedio de la primera lista esta por debajo del promedio total'
    elif promedioLista(lista2) == promedioListas2:
        return 'El promedio de la lista y el promedio total son iguales'
    else:
        promedioLista(lista2) > promedioTotal
        return 'El promedio de la segunda lista esta por encima del promedio total'

def numeroPar(lista):
    par=0
    for i in lista:
        if i % 2 == 0:
            par+=1
    return par

def numeroImpar(lista):
    impar=0
    for i in lista:
        if i % 2 == 1:
            impar+=1
    return impar

def mayorPar():
    mayorPares = 0
    if numeroPar(lista1) > numeroPar(lista2):
        mayorPares = numeroPar(lista1)
        return f"La lista que tiene mas pares es la lista 1: {numeroPar(lista1)}"
    else:
        mayorPares = numeroPar(lista2)
    return  f"La lista que tiene mas pares es la lista 2: {numeroPar(lista2)}"

def mayorImpar():
    mayorImpares = 0
    if numeroImpar(lista1) > numeroImpar(lista2):
        mayorImpares = numeroImpar(lista1)
        return f"La lista que tiene mas impares es la lista 1: {numeroImpar(lista1)}"
    else:
        mayorImpares = numeroImpar(lista2)
    return f"La lista que tiene mas impares es la lista 2: {numeroImpar(lista2)}"

lista1= llenarLista(tam, rango)
print("La lista 1 contiene", len(lista1), "numeros")
print(lista1)
print(f"La suma de la lista 1 es:", sumaLista(lista1))
print(f"El numero mayor de la lista es:", mayorLista(lista1))
print(f"El numero menor de la lista es:", menorLista(lista1))
print(f"El promedio de la lista es:", promedioLista(lista1))
print(f"La lista 1 tiene", numeroPar(lista1), "numeros pares")
print(f"La lista 1 tiene", numeroImpar(lista1), "numeros impares")

print ()

lista2= llenarLista(tam, rango)
print("La lista 2 contiene", len(lista2), "numeros")
print(lista2)
print(f"La suma de la lista 2 es:", sumaLista(lista2))
print(f"El numero mayor de la lista es:", mayorLista(lista2))
print(f"El numero menor de la lista es:", menorLista(lista2))
print(f"El promedio de la lista es:", promedioLista(lista2))
print(f"La lista 2 tiene", numeroPar(lista2), "numeros pares")
print(f"La lista 2 tiene", numeroImpar(lista2), "numeros impares")

print ()

print(sumaMayor(lista1, lista2))
print(mayorListas(lista1,lista2))
print(menorListas(lista1,lista2))
print(promedioListas1(lista1,lista2))
print(promedioListas2(lista1,lista2))
print(mayorPar())
print(mayorImpar())