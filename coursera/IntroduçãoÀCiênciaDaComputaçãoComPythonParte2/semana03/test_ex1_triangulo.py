from ex1_triangulo import Triangulo
import pytest

class Test_Triangulo:
    @pytest.fixture
    def t(self):
        return Triangulo(1,1,1)

    def test_a(self,t):
        assert t.a == 1

    def test_b(self,t):
        assert t.b == 1

    def test_c(self,t):
        assert t.c == 1

    def test_perimetro(self,t):
        assert t.perimetro() == 3

    