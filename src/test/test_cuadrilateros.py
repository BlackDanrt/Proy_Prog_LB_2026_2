import unittest

import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

from cuadrilateros.area import (
    area_trapecio,
    area_trapecio_rectangulo,
    area_trapecio_isosceles,
    area_trapecio_escaleno,
    area_paralelogramo,
    area_romboide,
    area_rombo,
    area_rectangulo,
    area_cuadrado,
)
from cuadrilateros.perimetro import calcularPerimetro
from cuadrilateros.clasificacion.clasificacion import clasificar_cuadrilatero
from cuadrilateros import graphic


class TestAreaCuadrilateros(unittest.TestCase):

    def test_trapecios(self):
        self.assertEqual(area_trapecio(6, 4, 3), 15)
        self.assertEqual(area_trapecio_rectangulo(6, 4, 3), 15)
        self.assertEqual(area_trapecio_isosceles(6, 4, 3), 15)
        self.assertEqual(area_trapecio_escaleno(6, 4, 3), 15)

    def test_trapecio_bases_iguales(self):
        with self.assertRaises(ValueError):
            area_trapecio(5, 5, 3)

    def test_paralelogramo_y_romboide(self):
        self.assertEqual(area_paralelogramo(5, 3), 15)
        self.assertEqual(area_romboide(5, 3), 15)

    def test_rombo(self):
        self.assertEqual(area_rombo(6, 4), 12)

    def test_rectangulo_y_cuadrado(self):
        self.assertEqual(area_rectangulo(5, 3), 15)
        self.assertEqual(area_cuadrado(4), 16)

    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            area_trapecio(6, 4, 0)
        with self.assertRaises(ValueError):
            area_paralelogramo(-5, 3)
        with self.assertRaises(ValueError):
            area_rombo(6, 0)
        with self.assertRaises(ValueError):
            area_rectangulo(0, 3)
        with self.assertRaises(ValueError):
            area_cuadrado(-1)


class TestPerimetroCuadrilatero(unittest.TestCase):

    def test_cuadrado(self):
        self.assertAlmostEqual(calcularPerimetro(0, 0, 4, 0, 4, 4, 0, 4), 16.0, places=3)

    def test_romboide(self):
        self.assertAlmostEqual(calcularPerimetro(0, 0, 4, 0, 5, 3, 1, 3), 14.325, places=3)

    def test_puntos_colineales(self):
        with self.assertRaises(ValueError):
            calcularPerimetro(0, 0, 2, 0, 4, 0, 2, 3)

    def test_puntos_repetidos(self):
        with self.assertRaises(ValueError):
            calcularPerimetro(0, 0, 0, 0, 4, 4, 0, 4)

    def test_lados_cruzados(self):
        with self.assertRaises(ValueError):
            calcularPerimetro(0, 0, 4, 4, 4, 0, 0, 4) 


class TestClasificacionCuadrilateros(unittest.TestCase):

    def test_paralelogramos(self):
        self.assertEqual(clasificar_cuadrilatero(0, 0, 4, 0, 4, 4, 0, 4), "cuadrado")
        self.assertEqual(clasificar_cuadrilatero(0, 0, 6, 0, 6, 3, 0, 3), "rectángulo")
        self.assertEqual(clasificar_cuadrilatero(0, 0, 2, 1, 4, 0, 2, -1), "rombo")
        self.assertEqual(clasificar_cuadrilatero(0, 0, 4, 0, 5, 3, 1, 3), "romboide")

    def test_trapecios(self):
        self.assertEqual(clasificar_cuadrilatero(0, 0, 6, 0, 3, 3, 0, 3), "trapecio rectángulo")
        self.assertEqual(clasificar_cuadrilatero(0, 0, 6, 0, 4, 3, 2, 3), "trapecio isósceles")
        self.assertEqual(clasificar_cuadrilatero(0, 0, 7, 0, 5, 3, 1, 3), "trapecio escaleno")

    def test_trapezoide(self):
        self.assertEqual(clasificar_cuadrilatero(0, 0, 4, 0, 5, 3, 1, 4), "trapezoide")

    def test_concavo(self):
        self.assertEqual(clasificar_cuadrilatero(0, 0, 4, 2, 0, 4, 1, 2), "cóncavo")

    def test_orden_horario_y_antihorario(self):
        self.assertEqual(clasificar_cuadrilatero(0, 0, 0, 4, 4, 4, 4, 0), "cuadrado")

    def test_invalidos(self):
        with self.assertRaises(ValueError):
            clasificar_cuadrilatero(0, 0, 2, 0, 4, 0, 2, 3)
        with self.assertRaises(ValueError):
            clasificar_cuadrilatero(0, 0, 4, 4, 4, 0, 0, 4)


class TestGraficosCuadrilateros(unittest.TestCase):

    def tearDown(self):
        plt.close("all")

    def test_grafico_valido(self):
        graphic.graficar_cuadrilatero(0, 0, 4, 0, 5, 3, 1, 3)
        graphic.graficar_cuadrilatero(0, 0, 4, 2, 0, 4, 1, 2)

    def test_area_por_coordenadas(self):
        self.assertEqual(graphic._area_coordenadas([(0, 0), (4, 0), (4, 3), (0, 3)]), 12)
        self.assertEqual(graphic._area_coordenadas([(0, 0), (4, 2), (0, 4), (1, 2)]), 6)

    def test_grafico_invalido(self):
        with self.assertRaises(ValueError):
            graphic.graficar_cuadrilatero(0, 0, 4, 4, 4, 0, 0, 4)


if __name__ == "__main__":
    unittest.main()