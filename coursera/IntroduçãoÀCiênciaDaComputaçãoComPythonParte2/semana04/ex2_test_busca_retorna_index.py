from ex2_busca_retorna_index import Busca
import pytest

class Test_Busca:
    @pytest.fixture
    def b(self):
        return Busca()

    def test_busca_01(self,b):
        '''Search for letter 'e' and returns the index'''
        assert b.busca(['a','e','i'],'e') == 1

    def test_busca_02(self,b):
        '''Search for letter 'u' and returns False'''
        assert b.busca(['a','e','i'],'u') == False

    def test_busca_03(self,b):
        '''Search for number '10' and returns the index'''
        assert b.busca([5,6,7,8,9,10,11],10) == 5

    def test_busca_04(self,b):
        '''Search for number '12' and returns False'''
        assert b.busca([5,6,7,8,9,10,11],12) == False