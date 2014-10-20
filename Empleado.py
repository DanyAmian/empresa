__author__ = 'Daniel'

class Empleado:
    def __init__(self,nombre,apellidos,dni,direccion,edad,email,salario):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.direccion=direccion
        self.edad=edad
        self.email=email
        self.salario=salario

    def getSalario(self):
        return "El salario es: "+self.salario
    def getDni(self):
        return "El DNI es: "+self.dni
    def getNombre(self):
        return self.nombre+" "+self.apellidos
