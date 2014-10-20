from unittest import TestCase
from mockito import *
from Empleado import *
from Departamento import *


__author__ = 'aulas'


class TestDepartamento(TestCase):
    def test_getSalarioTotal(self):
        # Generate a mock from a class
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        dept = Departamento("Calidad",1)
        # Mock method calls
        when(emp1).getSalario().thenReturn(1000)
        when(emp2).getSalario().thenReturn(2000)
        when(emp3).getSalario().thenReturn(3000)

        dept.aniadirEmpleado(emp1)
        dept.aniadirEmpleado(emp2)
        dept.aniadirEmpleado(emp3)

        res=dept.getSalarioTotal()
        print("Salario emp1: "+str(emp1.getSalario()))
        print("Salario emp2: "+str(emp2.getSalario()))
        print("Salario emp3: "+str(emp3.getSalario()))
        print("Salario total devuelto por getSalarioTotal(): "+str(res))
        self.assertEquals(res,6000)