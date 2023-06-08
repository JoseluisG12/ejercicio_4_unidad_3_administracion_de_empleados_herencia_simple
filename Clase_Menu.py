
class Menu:
    __switcher = None

    def __init__(self)->None:
        self.__switcher = {1:self.op1,
                           2:self.op2,
                           3:self.op3,
                           4:self.op4,
                        }

    def run(self,Mempleados):
        band = True
        while band:
            b = int(input("""
Menu Principal:
1-registrar las horas trabajadas segun DNI
2-total de tareas terminadas
3-listar a empleados q necesite la ayuda economica 
4-conocer el sueldo general a pagar por empleado
\n"""))
            func = self.__switcher.get(b)
            if func:
                 func(Mempleados)
            else:
                print("Saliendo...")
                band = False
    def op1(self,Mempleados):
        Mempleados.registrarhora()

    def op2(self,Mempleados):
        Mempleados.tareasterminadas()

    def op3(self,Mempleados):
        Mempleados.ayudaeconomica()

    def op4(self,Mempleados):
        Mempleados.sueldosgeneral()
