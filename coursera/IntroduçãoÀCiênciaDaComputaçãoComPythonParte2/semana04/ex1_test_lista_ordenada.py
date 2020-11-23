from ex1_lista_ordenada import Sorting
import pytest

class Test_Sorting:
    @pytest.fixture
    def l(self):
        return Sorting()

    def test_input(self,l):
        assert l.getting_list([8,9,-7,3,0]) == [8,9,-7,3,0]

    def test_ordering_01(self,l):
        '''All different values and out of order'''
        assert l.direct_order_list([8,9,-7,3,0]) == [-7,0,3,8,9]

    def test_ordering_02(self,l):
        '''All different values and one at correct position'''
        assert l.direct_order_list([-8,9,-7,3,0]) == [-8,-7,0,3,9]
        
    def test_ordering_03(self,l):
        '''Two equal values'''
        assert l.direct_order_list([-8,9,-7,9,0]) == [-8,-7,0,9,9]

    def test_checking_order_01(self,l):
        '''Input list out of order'''
        assert l.ordenada([-8,9,-7,9,0]) == False

    def test_checking_order_02(self,l):
        '''Input list ordered'''
        assert l.ordenada([-8,-7,0,9,9]) == True
        