dicc={'ciudad':'Bogota',
     'continente':'Asia',
     'planeta':'Marte',
     'pais':'España'}



def clave (key, diccionario):
    if key  in diccionario:        
        
        if key in diccionario:
            l1= diccionario [key]
            l2 = type(l1)
            if l2 is str:
             l2 = " cadena"
            else:
             l2= " entero"
            
        return f"La palabra {key} esta asociada a  {l1} y es de tipo {l2}"
    else: 
       return f"La clave {key} no esta en el diccionario"
print(clave(input("Escriba la clave a buscar: "), dicc))