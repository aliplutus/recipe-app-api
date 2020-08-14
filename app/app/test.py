from django.test import TestCase
from app.calc import add, subtract


class CalcTest(TestCase):
    def test_add_numbers(self):
        """test the tow variables x and y"""
        self.assertEqual(add(3, 8), 11)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)
