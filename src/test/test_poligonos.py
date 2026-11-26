import math
import unittest

import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

from poligonos.area import area_poligono, area_poligono_regular, area_poligono_regular_apotema
from poligonos.perimetro import calcularPerimetro, perimetro_poligono_regular
from poligonos.clasificacion.clasificacion_poligonos import clasificar_por_forma, clasificar_por_lados
from poligonos.diagonales.diagonales import (
    numero_total_diagonales,
    diagonales_desde_un_vertice,
    diagonales_desde_m_vertices,
)
from poligonos.especiales.poligonos_especiales import es_equilatero, es_equiangulo
from poligonos import graphic

CUADRADO = [(0, 0), (4, 0), (4, 4), (0, 4)]
RECTANGULO = [(0, 0), (6, 0), (6, 3), (0, 3)]
ROMBO = [(0, 0), (2, 1), (4, 0), (2, -1)]
FLECHA = [(0, 0), (4, 2), (0, 4), (1, 2)]  
HEXAGONO = [(math.cos(k * math.pi / 3), math.sin(k * math.pi / 3)) for k in range(6)]


class TestClasificacionPoligonos(unittest.TestCase):

    def test_por_forma(self):
        self.assertEqual(clasificar_por_forma(CUADRADO), "convexo")
        self.assertEqual(clasificar_por_forma(HEXAGONO), "convexo")
        self.assertEqual(clasificar_por_forma(FLECHA), "cóncavo")

    def test_por_lados(self):
        self.assertEqual(clasificar_por_lados(3), "triángulo")
        self.assertEqual(clasificar_por_lados(5), "pentágono")
        self.assertEqual(clasificar_por_lados(20), "icoságono")
        self.assertEqual(clasificar_por_lados(25), "polígono de 25 lados")

    def test_por_lados_invalido(self):
        with self.assertRaises(ValueError):
            clasificar_por_lados(2)
        with self.assertRaises(ValueError):
            clasificar_por_lados(4.0)
        with self.assertRaises(ValueError):
            clasificar_por_lados(True)


class TestAreaPoligonos(unittest.TestCase):

    def test_area_coordenadas(self):
        self.assertEqual(area_poligono(CUADRADO), 16)
        self.assertEqual(area_poligono(FLECHA), 6)
        self.assertAlmostEqual(area_poligono(HEXAGONO), 2.598, places=3)

    def test_area_no_depende_del_sentido(self):
        self.assertEqual(area_poligono(CUADRADO), area_poligono(CUADRADO[::-1]))

    def test_area_regular(self):
        self.assertAlmostEqual(area_poligono_regular(4, 3), 9, places=3)
        self.assertAlmostEqual(area_poligono_regular(6, 1), 2.598, places=3)

    def test_area_regular_apotema(self):
        self.assertAlmostEqual(area_poligono_regular_apotema(6, 1, math.sqrt(3) / 2), 2.598, places=3)

    def test_area_invalida(self):
        with self.assertRaises(ValueError):
            area_poligono([(0, 0), (1, 1)])
        with self.assertRaises(ValueError):
            area_poligono_regular(2, 3)
        with self.assertRaises(ValueError):
            area_poligono_regular(5, 0)
        with self.assertRaises(ValueError):
            area_poligono_regular_apotema(5, 2, -1)


class TestPerimetroPoligonos(unittest.TestCase):

    def test_perimetro_coordenadas(self):
        self.assertEqual(calcularPerimetro(CUADRADO), 16)
        self.assertAlmostEqual(calcularPerimetro(HEXAGONO), 6, places=3)

    def test_perimetro_regular(self):
        self.assertEqual(perimetro_poligono_regular(6, 2), 12)

    def test_perimetro_invalido(self):
        with self.assertRaises(ValueError):
            calcularPerimetro([(0, 0), (2, 2), (2, 0), (0, 2)])  
        with self.assertRaises(ValueError):
            perimetro_poligono_regular(6, -2)


class TestDiagonales(unittest.TestCase):

    def test_total(self):
        self.assertEqual(numero_total_diagonales(3), 0)
        self.assertEqual(numero_total_diagonales(4), 2)
        self.assertEqual(numero_total_diagonales(6), 9)
        self.assertEqual(numero_total_diagonales(10), 35)

    def test_desde_un_vertice(self):
        self.assertEqual(diagonales_desde_un_vertice(3), 0)
        self.assertEqual(diagonales_desde_un_vertice(8), 5)

    def test_desde_m_vertices(self):
        resultados = [diagonales_desde_m_vertices(6, m) for m in range(1, 7)]
        self.assertEqual(resultados, [3, 6, 8, 9, 9, 9])

    def test_desde_un_vertice_coincide_con_m_igual_1(self):
        for n in range(3, 15):
            self.assertEqual(diagonales_desde_m_vertices(n, 1), diagonales_desde_un_vertice(n))

    def test_invalidos(self):
        with self.assertRaises(ValueError):
            numero_total_diagonales(2)
        with self.assertRaises(ValueError):
            diagonales_desde_un_vertice(5.5)
        with self.assertRaises(ValueError):
            diagonales_desde_m_vertices(6, 0)
        with self.assertRaises(ValueError):
            diagonales_desde_m_vertices(6, 7)


class TestPoligonosEspeciales(unittest.TestCase):

    def test_equilatero(self):
        self.assertTrue(es_equilatero(CUADRADO))
        self.assertTrue(es_equilatero(ROMBO))
        self.assertTrue(es_equilatero(HEXAGONO))
        self.assertFalse(es_equilatero(RECTANGULO))

    def test_equiangulo(self):
        self.assertTrue(es_equiangulo(CUADRADO))
        self.assertTrue(es_equiangulo(RECTANGULO))
        self.assertTrue(es_equiangulo(HEXAGONO))
        self.assertFalse(es_equiangulo(ROMBO))
        self.assertFalse(es_equiangulo(FLECHA))


class TestValidacionPoligono(unittest.TestCase):

    def test_poligonos_invalidos(self):
        casos = [
            [(0, 0), (1, 1)],                     
            [(0, 0), (1, "a"), (2, 2)],           
            [(0, 0), (1, 0), (0, 0), (0, 1)],     
            [(0, 0), (1, 0), (2, 0), (1, 1)],     
            [(0, 0), (2, 2), (2, 0), (0, 2)],     
        ]
        for vertices in casos:
            with self.subTest(vertices=vertices):
                with self.assertRaises(ValueError):
                    area_poligono(vertices)


class TestGraficosPoligonos(unittest.TestCase):

    def tearDown(self):
        plt.close("all")

    def test_graficos_validos(self):
        graphic.graficar_poligono(FLECHA)
        graphic.graficar_diagonales(HEXAGONO, 2)
        graphic.graficar_poligono_regular(8, 1.5)

    def test_vertices_poligono_regular(self):
        vertices = graphic.vertices_poligono_regular(5, 2)
        self.assertEqual(len(vertices), 5)
        self.assertTrue(es_equilatero(vertices))
        self.assertTrue(es_equiangulo(vertices))
        self.assertAlmostEqual(calcularPerimetro(vertices), 10, places=3)

    def test_graficos_invalidos(self):
        with self.assertRaises(ValueError):
            graphic.graficar_poligono([(0, 0), (2, 2), (2, 0), (0, 2)])
        with self.assertRaises(ValueError):
            graphic.graficar_diagonales(CUADRADO, 5)
        with self.assertRaises(ValueError):
            graphic.graficar_poligono_regular(2, 1)


if __name__ == "__main__":
    unittest.main()