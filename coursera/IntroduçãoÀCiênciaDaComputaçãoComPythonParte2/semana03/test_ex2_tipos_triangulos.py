from ex2_tipos_triangulos import Triangulo
import pytest

class Test_Triangulo:
    def test_equilatero(self):
        t = Triangulo (4,4,4)
        assert t.tipo_lado() == 'equilátero'

    def test_escaleno(self):
        t = Triangulo (3,4,5)
        assert t.tipo_lado() == "escaleno"

    def test_isosceles(self):
        t = Triangulo (2,4,2)
        assert t.tipo_lado() == "isósceles"
