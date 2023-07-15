from Paciente import *
class Medico(Paciente):
    def __init__(self, nombreMedico, documento, disponibilidad, consultorio):
        self.__nombreMedico =nombreMedico
        self.__documento = documento
        self.__desponibilidad = disponibilidad
        self.__consultorio = consultorio

    def consultarCitasAgendadas():
        print("___Consulta de Citas Agendadas___")
        buscarCita = input("Ingresar el nombre del paciente con el que se registro la cita: ")
        for cita in Paciente.lcitas:
            if buscarCita  == cita["Nombre del paciente: "]:
               print("Cita encontradacon exito:  ")
               print("Pacinte: ", Paciente.dcitas ["Nombre del paciente: "])
               print("Medico: ", Paciente.dcitas["Nombre del medico: "])
               print("Hora de agendacion: ", Paciente.dcitas["Hora de agendacion: "] )
               print("Nombre del consultorio: ", Paciente.dcitas["Nombre del consultorio: "])
               print("motivo de la consulta: ", Paciente.dcitas["Motivo de la consulta: "])
            else:
                print ("No se encontro una cita con el nombre", buscarCita)



def mostrarMedico(self):
        return f'{self.__nombre},{self.__documento}, {self.__disponibilidad}, {self.__consultorio}'