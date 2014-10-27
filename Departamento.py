__author__ = 'Daniel'


class Departamento:
    def __init__(self, nombre_depto, id_depto):
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.lista_empleados = []

    def get_nombre_depto(self):
        return self.nombre_depto

    def get_id_depto(self):
        return self.id_depto

    def aniadir_empleado(self, empleado):
        self.lista_empleados.append(empleado)

    def get_salario_total(self):
        total = 0
        for empleado in self.lista_empleados:
            total += empleado.get_salario()
        return total

    # #EPD3
    def get_salario_total_mensual(self):
        total = 0
        for empleado in self.lista_empleados:
            total += empleado.get_salario_mensual()
        return total