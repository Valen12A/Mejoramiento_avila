from Paciente import *
from Medico import *
from Cita import *

while True:
    print("__MENU___")
    print("1. Paciente")
    print("2. Medico")
    print("3. Salir")
    
    opcion = int(input("Elija una opcion del menu principal: "))
    
    if opcion == 1:
        print()
        print("__MENU PACIENTE__")
        print("1. Registrar cita")
        print("2. Consultar cita")
        print("3. Eliminar cita")
        print("4. Seleccionar especialidad")
        
        opcionPaciente = int(input('Elija una opcion del menu paciente : '))
        
        if opcionPaciente == 1:
            Paciente.registrarCita(Paciente.lcitas)
        elif opcionPaciente == 2:
            Paciente.consultarCita()
        elif opcionPaciente == 3:
            Paciente.eliminarCita()
        elif opcionPaciente == 4:
            Paciente.seleccionarEspecialidad()
        else:
            print("Ingresar opcion valida")
    
    elif opcion != 1 or 3:
        print("__MENU MEDICO__")
        print("1. Consultar cita agendada")
        
        opcionMedico = int(input('Elija una opcion del menu medico: '))
        
        if opcionMedico == 1:
            Medico.consultarCitasAgendadas()
        else:
            print('Ingresar opcion válida')
    
    elif opcion != 1 or 2:
        break
    
    else:
        print("Ingresar opcion válida")
