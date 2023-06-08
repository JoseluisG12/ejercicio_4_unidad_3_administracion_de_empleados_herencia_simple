from Clase_Empleado import Empleado
class Empleado_Contratado(Empleado):
    __fecha : str
    __finalizacion_contrato : str
    __hora_trabajadas : str
    __valor_x_hora : float

    def __init__(self,DNI,nombre,direccion,telefono,fecha,contrato,horas,valor)->None:
        Empleado.__init__(self,DNI,nombre,direccion,telefono)
        self.__fecha = fecha
        self.__finalizacion_contrato = contrato
        self.__hora_trabajadas = int(horas)
        self.__valor_x_hora = int(valor)

    def sueldo(self):
        return self.__hora_trabajadas * self.__valor_x_hora

    def sethoras(self,horas):
        self.__hora_trabajadas += horas

    def __str__(self):
        return f"""
dni:{super().getdni()}
nombre: {super().getnombre()}
direccion: {super().getdireccion()} 
telefono: {super().gettelefono()} 
fecha :{self.__fecha}
finalizacion del contrato:{self.__finalizacion_contrato}
horas trabajadas:{self.__hora_trabajadas}
valor por hora:{self.__valor_x_hora}"""