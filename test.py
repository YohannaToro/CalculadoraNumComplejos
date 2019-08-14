import unittest

from calculadora import *

class TestDijkstra(unittest.TestCase):
    def test_suma_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result = suma_complejos((5,2),(-8,3))
        self.assertEqual(result, (-3,5))
    def test_resta_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result = resta_complejos((5,2),(4,-2))
        self.assertEqual(result, (1,4))
    def test_producto_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result = producto_complejos((1,2),(5,-2))
        self.assertEqual(result, (9,8))
    def test_division_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result =division_complejos((5,-3),(2,1))
        self.assertEqual(result,(1.4, -2.2))
    def test_modulo_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result =modulo_complejos((8,-3))
        self.assertEqual(result,8.54400374531753)
    def test_polarCartesiano_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result = suma_complejos((5,2),(-8,3))
        self.assertEqual(result, (-3,5))
    def test_CartesianoPolar_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result = suma_complejos((5,2),(-8,3))
        self.assertEqual(result, (-3,5))
    def test_conjugado_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result =conjugado_complejos((8,-12))
        self.assertEqual(result, (8, 12))
    def test_fase_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result =fase_complejo((9,-5))
        self.assertEqual(result,-29.05)
    


if __name__ == '__main__':
    unittest.main()
