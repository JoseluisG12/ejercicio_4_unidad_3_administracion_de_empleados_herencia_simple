from Manejador_Empleados import Arreglo_Empleados
from Clase_Menu import  Menu

if __name__=='__main__':
    opc = input("desea probar los metodos con la funcion test y = si n = no\n")
    if opc == 'y':
        opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
        while opc != 0:
            if opc == 1:
                Mempleados = Arreglo_Empleados(3)
                Mempleados.test()
                Mmenu = Menu()
                Mmenu.run(Mempleados)
            if opc == 2:
                Mempleados = Arreglo_Empleados(3)
                Mempleados.testDatoserroneos()
                Mmenu = Menu()
                Mmenu.run(Mempleados)
            opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))

        print("_______main_________")
    cantidad = int(input("ingrese la cantidad de empleados a registrar\n"))
    Mempleados = Arreglo_Empleados(cantidad)
    Mempleados.cargaempleados()
    menu = Menu()
    menu.run(Mempleados)

