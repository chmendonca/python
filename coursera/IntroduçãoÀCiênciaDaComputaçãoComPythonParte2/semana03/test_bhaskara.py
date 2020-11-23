from calcula_raizes import Bhaskara
import pytest #allows to use the fixture

class TestBhaskara:
    # @pytest.fixture
    # def b(self):
    #     return Bhaskara()

    def testa_uma_raiz(self):
        bkra = Bhaskara(1,0,0)
        #x ^ 2 = 0
        #a resposta é uma raiz e o valor é 2
        assert (bkra.calcula_raizes() == (1,0))

    def testa_duas_raizes(self):
        bkra = Bhaskara(1,-5,6)
        #x ^ 2 - 5 * x + 6 = 0
        #a resposta são duas raízes e os valores são 3 e 2
        assert (bkra.calcula_raizes() == (2, 3, 2))

    def testa_nao_possui_raizes_reais(self):
        bkra = Bhaskara(10,10,10)
        #10 * x ^ 2 + 10 * x + 10 = 0
        #a resposta é 0
        assert (bkra.calcula_raizes() == (0))

    def testa_raiz_negativa(self):
        bkra = Bhaskara(10,20,10)
        #10* x ^ 2 + 20 * x + 10 = 0
        #a resposta são duas raízes e os valores são 3 e 2
        assert (bkra.calcula_raizes() == (1, -1))