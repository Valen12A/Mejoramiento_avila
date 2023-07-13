from Paciente import *
class Medico(Paciente):
    def __init__(self, nombreMedico, documento, disponibilidad, consultorio):
        self.__nombreMedico =nombreMedico
        self.__documento = documento
        self.__desponibilidad = disponibilidad
        self.__consultorio = consultorio

def consultarCitasAgendadas ():

        for Paciente.dcitas in Paciente.lcitas:
            buscarCita = input('Ingrese el nombre del paciente que tiene la cita: ')
            if Paciente.Cit["Nombre del Paciente"] == buscarCita:
                print("Cita encontrada:")
                print("Medico: ", Paciente.dcitas["nombreMedico"])
                print("Nombre del consultorio: ", Paciente.dcitas["nombreConsultorio"])
                print("motivo de la consulta: ", Paciente.dcitas["motivoConsulta"])
                print("Fecha de agendación : ", Paciente.dcitas["fechaAgenda"])

            else:
                print("Cita no encontrada.")    



def getMedico(self):
        return f'{self.__nombre},{self.__documento}, {self.__disponivilidad}, {self.__consultorio}'