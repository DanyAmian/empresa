__author__ = 'Daniel'

class Departamento:
    def __init__(self,nombreDepto,idDepto):
        self.nombreDepto=nombreDepto
        self.idDepto=idDepto
        self.listaEmpleados=[]

    def get_nombre_depto(self):
        return self.nombreDepto
    def getIdDepto(self):
        return self.idDepto
    def aniadirEmpleado(self,empleado):
        self.listaEmpleados.append(empleado)
    def getSalarioTotal(self):
        total=0
        for empleado in self.listaEmpleados:
            total+=empleado.getSalario()
        return total
    ##EPD3
    def get_salario_total_mensual(self):
        total=0
        for empleado in self.listaEmpleados:
            total+=empleado.get_salario_mensual()
        return total