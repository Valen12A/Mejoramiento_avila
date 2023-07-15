class Cita ():
    def __init__(self,nombreMedico, diaCita, mesCita, añoCita, horaCita, motivoConsulta,  nombreConsultorio):
        self.__diaCita = diaCita
        self.__mesCita = mesCita
        self.__añoCita = añoCita
        self.__horaCita = horaCita
        self.__motivoConsulta = motivoConsulta
        self.__nombreConsultorio = nombreConsultorio
        self.__nombreMedico = nombreMedico
    



def mostarCita(self):
        return f'{self.__facheAgenda}, {self.__motivoConsulta}, {self.__consultorio}, {self.__horarioDisponible}'
        