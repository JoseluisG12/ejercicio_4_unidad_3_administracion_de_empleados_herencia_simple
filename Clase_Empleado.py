
class Empleado:
    __DNI : int
    __nombre : str
    __direccion : str
    __telefono : int

    def __init__(self,DNI,nombre,direccion,telefono)->None:
        self.__DNI = int(DNI)
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def getdni(self):
        return self.__DNI

    def getnombre(self):
        return self.__nombre

    def getdireccion(self):
        return self.__direccion

    def gettelefono(self):
        return self.__telefono
