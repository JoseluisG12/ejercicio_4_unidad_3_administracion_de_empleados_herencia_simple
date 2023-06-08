import numpy as np
from Clase_Empleado import Empleado
import csv
from Clase_EmpleadoPlanta import Empleado_Planta
from Clase_EmpleadoExterno import  Empleado_Externo
from Clase_EmpleadoContratado import Empleado_Contratado
from datetime import datetime
from Clase_Menu import Menu
class Arreglo_Empleados:
    __cantidad = 0
    __dimension = 0
    __incremento = 1
    __empleados : object

    def __init__(self,dimension = 10) ->None:
        self.__empleados = np.empty(dimension,dtype=Empleado)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarempleado(self,unEmpleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__empleados.resize(self.__dimension,refcheck=False)
        self.__empleados[self.__cantidad] = unEmpleado
        self.__cantidad += 1

    def cargaempleados(self):
        self.cargaEmpleadosPlanta()
        self.cargaEmpleadosContratado()
        self.cargaEmpleadosExternos()
        print("Empleados cargados con exito")

    def cargaEmpleadosPlanta(self):
        archivo = open('Planta.csv')
        reader = csv.reader(archivo,delimiter=(';'))
        next(reader)
        for fila in reader:
            empleado = Empleado_Planta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.agregarempleado(empleado)

        archivo.close()

    def cargaEmpleadosContratado(self):
        archivo = open('Contratados.csv')
        reader = csv.reader(archivo, delimiter=(';'))
        next(reader)
        for fila in reader:
            empleado = Empleado_Contratado(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5],fila[6],fila[7])
            self.agregarempleado(empleado)

        archivo.close()

    def cargaEmpleadosExternos(self):
        archivo = open('Externos.csv')
        reader = csv.reader(archivo, delimiter=(';'))
        next(reader)
        for fila in reader:
            empleado = Empleado_Externo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5],fila[6],fila[7],fila[8],fila[9])
            self.agregarempleado(empleado)

        archivo.close()


    def mostrar(self):
        for empleado in self.__empleados:
            print(str(empleado))

    def buscarempleado(self,DNI):
        band = True
        i = 0
        while band and i < len(self.__empleados):
            if self.__empleados[i].getdni() == DNI:
                band = False
            else:
                i = i + 1
        return self.__empleados[i]

    def registrarhora(self):
        DNI = int(input("ingrese el dni del empleado\n"))
        horas = int(input("ingrese la cantidad de horas a acumular\n"))
        empleado = self.buscarempleado(DNI)
        band = True
        while band:

            if isinstance(empleado,Empleado_Contratado):
                empleado.sethoras(horas)
                band = False
            else:
                print("el empleado ingresado no posee cantidad de horas trabajadas")
                DNI = int(input("ingrese el dni del empleado\n"))
                horas = int(input("ingrese la cantidad de horas a acumular\n"))
                empleado = self.buscarempleado(DNI)


    def buscartareas(self,tarea):
        total = 0
        fechaActual = datetime.now().date()
        fechaFormateada = fechaActual.strftime('%Y-%m-%d')
        for empleado in self.__empleados:
            if isinstance(empleado,Empleado_Externo)and empleado.gettarea() == tarea and empleado.gettareafin() < fechaFormateada:
               total += empleado.getcosto()

        return total


    def tareasterminadas(self):
        tarea = input("ingrese la tarea a verificiar\n")
        total = self.buscartareas(tarea)
        print(f"""
el Total de costo de obras no terminadas de {tarea} es: ${total}""")

    def ayudaeconomica(self):
        for empleado in self.__empleados:
            if isinstance(empleado,Empleado_Planta) and empleado.getsueldo() < 150000:
                print(f"""
Dni:{empleado.getdni()}
Nombre: {empleado.getnombre()}
Direccion:{empleado.getdireccion()}""")

    def sueldosgeneral(self):
        for empleado in self.__empleados:
            print(f"""
Nombre:{empleado.getnombre()}
telefono:{empleado.gettelefono()}
sueldo:${empleado.sueldo()}""")


    def test(self):
        print("__________carga_un_empleado_de_planta______________")
        empleado = Empleado_Planta(41230328,'jose','av.coratina',264567890,10000,5)
        self.agregarempleado(empleado)
        print("__________carga_un_empleado_con_contrato______________")
        empleado = Empleado_Contratado(40568765,'juan','chile 193',264509586,'20/4/2022','19/3/2023',400,500)
        self.agregarempleado(empleado)
        print("__________carga_un_empleado_externo______________")
        empleado = Empleado_Externo(35987567, 'ramiro','av.sarmiento',264098566,'carpinteria','2022/01/01','2022/02/28',200,200000,10000)
        self.agregarempleado(empleado)

    def testDatoserroneos(self):
        print("__________carga_un_empleado_de_planta______________")
        empleado = Empleado_Planta(41230328, 'jose', 'av.coratina', 264567890,'$10000', '5 años')
        self.agregarempleado(empleado)
        print("__________carga_un_empleado_con_contrato______________")
        empleado = Empleado_Contratado(40568765, 'juan', 'chile 193', 264509586, '20/4/2022', '19/3/2023', 400, 500)
        self.agregarempleado(empleado)
        print("__________carga_un_empleado_externo______________")
        empleado = Empleado_Externo(35987567, 'ramiro', 'av.sarmiento', 264098566, 'carpinteria', '2022/01/01',
                                    '2022/02/28', 200, 200000, 10000)
        self.agregarempleado(empleado)

