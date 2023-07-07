from Medico import *
from Paciente import *
class Cita (Paciente, Medico):
    def __init__(self, nombre, tipoDocumento, documento, disponibilidad, consultorio, fechaAgenda, motivoConsulta, especialidadMedico, nombreConsultorio, horarioDisponible):
        Paciente().__init__(nombre, tipoDocumento, documento)
        Medico().__init__(nombre, documento, disponibilidad, consultorio) 
        self.__fechaAgenda = fechaAgenda
        self.__motivoConsulta =motivoConsulta
        self.__especialidadMedico =especialidadMedico
        self.__nombreConsultorio = nombreConsultorio
        self.__horarioDisponible = horarioDisponible



def getCita(self):
        return f'{self.__nombre}, {self.__tipoDocumento},{self.__documento}, {self.__disponivilidad}, {self.__consultorio}, {self.__facheAgenda}, {self.__motivoConsulta}. {self.__especialidadMedico}, {self.__consultorio}, {self.__horarioDisponible}'