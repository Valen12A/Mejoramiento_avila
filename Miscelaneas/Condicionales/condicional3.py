'''En un juego de preguntas a las que se responde “Si” o “No” gana quien
responda correctamente las tres preguntas. Si se responde mal a cualquiera de
ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
1. ¿Colon descubrió América?
2. ¿La independencia de Colombia fue en el año 1810?
3. ¿The Doors fue un grupo de rock Americano?'''

print("Responde las siguientes preguntas con 'Si' o 'No' ")

p1 = input("¿Colon descubrió América?")
if p1 == "no":
     print ("Fin del juego")
else:
    p2 = input("¿La independencia de Colombia fue en el año 1810?")
    if p2 == "no":
     print ("Fin del juego")
    else: 
        p3 = input("¿The Doors fue un grupo de rock Americano?")
        if p3 == "no":
         print ("Fin del juego")
        else:
           print ("¡Felicidades has gando!")





