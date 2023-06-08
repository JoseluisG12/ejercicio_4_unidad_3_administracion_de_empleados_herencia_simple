from Clase_Empleado import Empleado
class Empleado_Planta(Empleado):
    __sueldo : float
    __antiguedad : int

    def __init__(self,DNI,nombre,direccion,telefono,sueldo,antiguedad)->None:
        Empleado.__init__(self,DNI,nombre,direccion,telefono)
        self.__sueldo = float(sueldo)
        self.__antiguedad = int(antiguedad)

    def getsueldo(self):
        return self.__sueldo

    def sueldo(self):
        return self.__sueldo + 1%(self.__sueldo*self.__antiguedad)

    def __str__(self):
        return f"""
dni:{super().getdni()}
nombre: {super().getnombre()}
direccion: {super().getdireccion()} 
telefono: {super().gettelefono()}
sueldo: {self.__sueldo}
antiguaedad: {self.__antiguedad}"""