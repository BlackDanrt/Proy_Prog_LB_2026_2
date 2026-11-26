import unittest

from validaciones import (
    validar_lados,
    validar_angulo,
    validar_radios,
    iguales,
    validar_numero_lados,
    producto_cruz,
    validar_poligono,
)


class TestValidaciones(unittest.TestCase):

    def test_validar_lados(self):
        validar_lados(1, 2.5, 100)  
        with self.assertRaises(ValueError):
            validar_lados(1, 0)
        with self.assertRaises(ValueError):
            validar_lados(-3)

    def test_validar_angulo(self):
        validar_angulo(90)
        with self.assertRaises(ValueError):
            validar_angulo(0)
        with self.assertRaises(ValueError):
            validar_angulo(180)

    def test_validar_radios(self):
        validar_radios(1, 2)
        with self.assertRaises(ValueError):
            validar_radios(0)

    def test_iguales(self):
        self.assertTrue(iguales(0.1 + 0.2, 0.3))   
        self.assertTrue(iguales(1e-16, 0))
        self.assertFalse(iguales(1, 1.001))

    def test_validar_numero_lados(self):
        validar_numero_lados(3)
        for invalido in (2, 0, -5, 4.0, "5", True):
            with self.subTest(n=invalido):
                with self.assertRaises(ValueError):
                    validar_numero_lados(invalido)

    def test_producto_cruz(self):
        self.assertGreater(producto_cruz((0, 0), (1, 0), (0, 1)), 0)   
        self.assertLess(producto_cruz((0, 0), (0, 1), (1, 0)), 0)      
        self.assertEqual(producto_cruz((0, 0), (1, 1), (2, 2)), 0)     

    def test_validar_poligono_valido(self):
        validar_poligono([(0, 0), (4, 0), (4, 3)])
        validar_poligono([(0, 0), (4, 2), (0, 4), (1, 2)])  


if __name__ == "__main__":
    unittest.main()