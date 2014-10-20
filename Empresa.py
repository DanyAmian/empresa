__author__ = 'Dany'

class Empresa:
    def __init__(self,nombre_empresa,cif,razon_social):
        self.nombre_empresa=nombre_empresa
        self.cif=cif
        self.razon_social=razon_social
        self.listaDepartamentos=[]

    def get_nombre_empresa(self):
        return self.nombre_empresa
    def get_cif(self):
        return self.cif
    def get_razon_social(self):
        return self.razon_social

    def aniadir_departamento(self,departamento):
        self.listaDepartamentos.append(departamento)