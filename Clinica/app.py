from Paciente import *
from Medico import *
from Cita import *


while True:
    print("__MENU___")
    print("1. Paciente")
    print("2. Medico")
    print("3. Salir")
    opcion = int(input("Ingrese las una opcion:"))
    if opcion == 1:
        print ()
        print("__MENU PACIENTE__")
        print("1. Registar cita")
        print("2. Consultar cita")
        print("3. Eliminar cita")
        print("4. Seleccionar especialidad")
        opcion = int(input('Elija una opcio:'))
        if opcion==0:
            break
        elif opcion == 1:
            Paciente.registrarCita(Paciente.lcitas)
        elif opcion == 2:
            Paciente.consultarCita()
        elif opcion == 3:
            Paciente.eliminarCita()
        elif opcion == 4:
            Paciente.seleccionarEspecialidad()
        else:
            print("Ingrese una opcion valida")
    if opcion == 2:
        print ("__MENU MEDICO__")
        print("1.Consultar cita agendada")
        opcion = int(input('Elija una opcion:'))
        if opcion ==0:
            break
        elif opcion == 1:
            Medico.ConsultarCitasAgendadas()
        else:
            print('Ingrese una opcion valida')