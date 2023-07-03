'''Calcular todos los números de 3 cifras tales que la suma
de los cubos de las cifras es igual al valor del número.'''
for i in range(100, 1000):           #numeros de 3 dijitos
    num = i
    u = num % 10
    num = num // 10
    d = num % 10
    c = num // 10
    cubo = (u**3)+(d**3)+(c**3)
    if cubo == i:
        print(f"{i} y la susma de sus cifras al cubo son iguales")


