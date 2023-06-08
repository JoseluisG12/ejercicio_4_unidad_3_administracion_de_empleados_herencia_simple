from Clase_Empleado import Empleado
class Empleado_Externo(Empleado):
    __tarea : str
    __fecha_inicio : str
    __fecha_finalizacion : str
    __viatico : float
    __costo_obra : float
    __seguro_vida : float

    def __init__(self,DNI,nombre,direccion,telefono,tarea,inicio,finalizacion,viatico,obra,seguro)->None:
        Empleado.__init__(self,DNI,nombre,direccion,telefono)
        self.__tarea = tarea
        self.__fecha_inicio = inicio
        self.__fecha_finalizacion = finalizacion
        self.__viatico = float(viatico)
        self.__costo_obra = float(obra)
        self.__seguro_vida = float(seguro)

    def sueldo(self):
        return (self.__costo_obra - self.__seguro_vida) - self.__viatico

    def gettarea(self):
        return self.__tarea

    def getcosto(self):
        return self.__costo_obra

    def gettareafin(self):
        return self.__fecha_finalizacion

    def __str__(self):
        return f"""
dni:{super().getdni()}
nombre: {super().getnombre()}
direccion: {super().getdireccion()} 
telefono: {super().gettelefono()}
tarea: {self.__tarea}
fecha de inicio: {self.__fecha_inicio}
fecha de finalizacion:{self.__viatico}
costo de la obra: {self.__costo_obra}
seguro de vida:{self.__seguro_vida}"""