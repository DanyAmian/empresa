__author__ = 'Daniel'

class Departamento:
    def __init__(self,nombreDepto,idDepto):
        self.nombreDepto=nombreDepto
        self.idDepto=idDepto
        self.listaEmpleados=[]

    def getNombreDepto(self):
        return "El departamento es: "+self.nombreDepto
    def getIdDepto(self):
        return "El id del departamento es: "+self.idDepto
    def aniadirEmpleado(self,empleado):
        self.listaEmpleados.append(empleado)
    def getSalarioTotal(self):
        total=0
        for empleado in self.listaEmpleados:
            total+=empleado.getSalario()
        return total