import unittest
from name_functions import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'."""

    def test_first_last_name(self):
        """Nomes como Janis Joplin funcionam?"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_name_mistake(self):
        """Nomes como Janis Joplin funcionam?"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertNotEqual(formatted_name,'Janis joplin')

    def test_leaving_first_name(self):
        """Nomes como Janis Joplin funcionam?"""
        formatted_name = get_formatted_name('q','joplin')
        self.assertEqual(formatted_name,'Q Joplin')

    def test_leaving_last_name(self):
        """Nomes como Janis Joplin funcionam?"""
        formatted_name = get_formatted_name('janis','q')
        self.assertEqual(formatted_name,'Janis Q')

    def test_first_middle_last_name(self):
        """Nomes como Janis Joplin funcionam?"""
        formatted_name = get_formatted_name('cassio','mendonça','henrique')
        self.assertEqual(formatted_name,'Cassio Henrique Mendonça')

    def test_first_middle_last_name_mistake(self):
        """Nomes como Janis Joplin funcionam?"""
        formatted_name = get_formatted_name('cassio','henrique','mendonça')
        self.assertNotEqual(formatted_name,'Cassio Henrique Mendonça')


unittest.main()