'''Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo
los cálculos así:
Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan
200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que
permita calcular el costo de una llamada dados los minutos de duración.'''



minutos = int(input("Ingrese los minutos: "))

if minutos == 3:
    print ("La llamda cuesta 200 pesos")
  
else:
    adicional = minutos - 3 
    val_min = 200 + (adicional * 50)

print("La llamada cuesta ", val_min, "pesos")
