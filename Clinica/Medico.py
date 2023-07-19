from Paciente import *
class Medico(Paciente):
    def __init__(self, nombreMedico, documento, disponibilidad, consultorio):
        self.__nombreMedico =nombreMedico
        self.__documento = documento
        self.__disponibilidad = disponibilidad
        self.__consultorio = consultorio

    def consultarCitasAgendadas():
        print()
        print("___Consulta de Citas Agendadas___")
        buscarCita = input("Ingresar el nombre del paciente: ")
        for cita in Paciente.lcitas:
            if buscarCita  == cita ["Nombre del paciente: "]:
               print("Cita encontrada con exito:  ")
               print("Paciente: ", Paciente.dcitas ["Nombre del paciente: "])
               print("Medico: ", Paciente.dcitas["Nombre del medico: "])
               print("Hora de agendacion: ", Paciente.dcitas["Hora de agendacion: "] )
               print("Nombre del consultorio: ", Paciente.dcitas["Nombre del consultorio: "])
               print("motivo de la consulta: ", Paciente.dcitas["Motivo de la consulta: "])
            else:
                print ("No se encontro una cita con el nombre", buscarCita)



def mostrarMedico(self):
        return f'{self.__nombreMedico},{self.__documento}, {self.__disponibilidad}, {self.__consultorio}'