from Cita import *
class Paciente(Cita):
    lcitas = []
    dcitas = {}
  
    def __init__(self, fechaAgenda, motivoConsulta, nombreConsultorio, nombrePaciente, tipoDocumento, documento):
        Cita().__init__  ( fechaAgenda, motivoConsulta, nombreConsultorio)
        self.__nombrePaciente = nombrePaciente 
        self.__tipoDocumento = tipoDocumento
        self.__documento = documento
        Paciente.lcitas = []
        Paciente.dcitas = {}
     


def registrarCita (Paciente):
     nombrePaciente = input("Ingresar el nombre del paciente: ")
     tipoDocumento = input("Ingresar el tipo de documento: ")
     documento = int(input("Ingresar el numero de documento: "))
     motivoConsulta = input("Ingresar el motivo de la consulta: ")
     fechaAgenda = int(input ("Ingresar la fecha agendada: "))
     nombreConsultorio = input ("Ingresar el nombre del consultorio: ")
     nombreMedico = input ("Ingresar el nombre del medico: ") 
     
     Paciente.dcitas= {"Nombre del paciente: " : nombrePaciente,
                      "Tipo de documento: " : tipoDocumento,
                      "Numero de documento: " : documento,
                      "Motivo de la consulta: " : motivoConsulta,
                      "Fecha de agendación: " : fechaAgenda,
                      "Nombre del consultorio: " : nombreConsultorio,
                      "Nombre del Medico: " : nombreMedico}
     Paciente.lcitas.append(Paciente.dcitas)
     print ("¡Cita registrada con exito!")

def consultarCita (Paciente):
     for Paciente.dcitas in Paciente.lcitas:
          buscarCita = input("Ingresar el nombre del paciente con el que se registro la cita: ")
          if Paciente.dcitas ["nombrePaciente"] == buscarCita:
               print("Medico: ", Paciente.dcitas["nombreMedico"])
               print("Nombre del consultorio: ", Paciente.dcitas["nombreConsultorio"])
               print("motivo de la consulta: ", Paciente.dcitas["motivoConsulta"])
               print("Fecha de agendación : ", Paciente.dcitas["fechaAgenda"])

def elimiarCita (Paciente):
     for Paciente.dcitas in Paciente.lcitas:
          eliminarCita = input("Ingresar el nombre del paciente con el que se registro la cita para eliminarla: ")
          if Paciente.dcitas["nombrePaciente"] == eliminarCita:
               Paciente.lcitas.remove (Paciente.dcitas)
     
def seleccionarEspecialidad(Paciente):
     especialidadesDisponibles = ["Odontologia", "Cardiologia", "Dermatologia", "Neurologia", "Pediatria", "Psicologia", "Ginecologia", "Oftalmologia", "Ortopedia"]
     print("Especialidades disponibles:", especialidadesDisponibles)
     for n, especialidad in enumerate(especialidadesDisponibles):
        print(f"{n + 1}. {especialidad}")
    
     ESeleccionadas = []

     while True:
        opcion = input("Selecciona una especialidad: ")        
        if opcion == "q":
            break
        
        try:
            opcion = int(opcion)
            if opcion < 1 or opcion > len(especialidadesDisponibles):
                print("Opción inválida")
                continue
            
            especialidadSeleccionada = especialidadesDisponibles[opcion - 1]
            
            if especialidadSeleccionada in ESeleccionadas:
                print("Esa especialidad ya ha sido seleccionada")
            else:
                ESeleccionadas.append(especialidadSeleccionada)
                print(f"Especialidad '{especialidadSeleccionada}' seleccionada.")
        
        except ValueError:
            print("Opción inválida. Intenta nuevamente.")
    
     print("Especialidades seleccionadas:")
     for especialidad in ESeleccionadas:
        print(especialidad)

     

def mostarPaciente(self):
        return f'{self.__nombre},{self.__tipoDocumento},{self.__documento}'


