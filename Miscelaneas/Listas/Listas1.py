#suma, promedio, minimo, maximo, moda, acendente, desendente, mediana.
import random
tam = 10
rango = 20
def llenarLista(tam,rango):
    lista=[]

    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):       
    sum=0                  
    for x in lista:          #Recore cada elemento de la lista. 
        sum+=x               #Suma acumulativa de todos los elementos de la lista.
    return sum

def promedioLista(lista):     
    return sumaLista(lista)/len(lista)  #Se divide la suma de la lista por la cantidad de elementos en ella.


def mayorLista(lista):        
    maximo = lista[0]                     #Se inicializa la variable aumiendo que el primer elemento es el mayor hasta el momento 
    for i in lista:
        if i > maximo:
            maximo=i
    return f"El numero mayor de la lista es: {maximo}"

def menorLista(lista):
    minimo=lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return f"El numero menor de la lista es: {minimo}"

def moda(lista):
    max=0
    for i in lista:
        cont=0
        for o in lista:
            if i == o:
                cont+=1
        if cont > max:
            max = cont
            moda1= i
    return f'La moda es: {moda1} ya que se repite {max}'


def ascendente(lista):
    aux=0
    for i in range(len(lista)):             #Posicion actual desde donde se comparan los elementos.
        for j in range(i+1,len(lista)):     #Se encarga de comparar la posicion i con el resto de la lista.
            if lista[i] > lista[j]:         #Compara la posicion i con la j, la posicicion j se remplaza con la i si j es menor. 
                aux = lista[i]              # i = aux, j = i, aux=j
                lista[i] = lista[j]
                lista[j] = aux
    return f"Lista1 ordenada ascendentemente{lista}"


def mediana(lista):
    if len(lista) %2!=0:                   #Se calcula el tamaño de la lista 
        aux = (len(lista)+1)//2            #Si es impar
        return lista[aux-1]
    else:
        aux  = (len(lista) - 1) // 2       #Si es par 
        aux1 = (lista [aux])
        aux2 = (lista[aux + 1])
        aux  = aux1 + aux2                 
        aux  = aux // 2
    return f"La mediana de la lista1 es: {aux}"

def descendente(lista):
    aux=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return f"Lista1 ordenada descendentemente{lista}"


lista1 = llenarLista (tam,rango)
print (lista1)
print ("La lista contiene", len(lista1), "numeros")
print(f"La suma de la lista 1 es:", sumaLista(lista1))
print(f"El promedio de la lista 1 es: ", promedioLista(lista1))
print(mayorLista(lista1))
print(menorLista(lista1))
print(moda(lista1))
print(ascendente(lista1))
print(mediana(lista1))
print(descendente(lista1))

