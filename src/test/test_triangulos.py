import math
import unittest

import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

from triangulos.area import (
    area_triangulo,
    area_triangulo_equilatero,
    area_triangulo_isosceles,
    area_triangulo_escaleno,
    area_triangulo_rectangulo,
    area_triangulo_acutangulo,
    area_triangulo_obtusangulo,
)
from triangulos.perimetro import calcularPerimetro
from triangulos.clasificacion.congruencia import clasificar_por_lados
from triangulos.clasificacion.congruencia_angulos import clasificar_por_angulos
from triangulos.calculo.notables import triangulo_notable
from triangulos.calculo.angulos_aproximados import triangulo_aproximado
from triangulos.congruentes.lll import congruencia_lll
from triangulos.congruentes.lal import congruencia_lal
from triangulos.congruentes.ala import congruencia_ala
from triangulos.congruentes.lla import congruencia_lla
from triangulos.teoremas.coseno import teorema_coseno
from triangulos import graphic


class TestAreaTriangulos(unittest.TestCase):

    def test_area_base_altura(self):
        self.assertEqual(area_triangulo(4, 3), 6)

    def test_area_equilatero(self):
        self.assertAlmostEqual(area_triangulo_equilatero(2), 1.732, places=3)

    def test_area_isosceles_acutangulo_obtusangulo(self):
        self.assertEqual(area_triangulo_isosceles(6, 4), 12)
        self.assertEqual(area_triangulo_acutangulo(6, 4), 12)
        self.assertEqual(area_triangulo_obtusangulo(6, 4), 12)

    def test_area_escaleno_heron(self):
        self.assertAlmostEqual(area_triangulo_escaleno(3, 4, 5), 6.0, places=3)
        self.assertAlmostEqual(area_triangulo_escaleno(5, 6, 7), 14.697, places=3)

    def test_area_rectangulo(self):
        self.assertEqual(area_triangulo_rectangulo(3, 4), 6)

    def test_lados_invalidos(self):
        with self.assertRaises(ValueError):
            area_triangulo(0, 3)
        with self.assertRaises(ValueError):
            area_triangulo(4, -1)
        with self.assertRaises(ValueError):
            area_triangulo_equilatero(-2)
        with self.assertRaises(ValueError):
            area_triangulo_rectangulo(3, 0)

    def test_escaleno_sin_desigualdad_triangular(self):
        with self.assertRaises(ValueError):
            area_triangulo_escaleno(1, 2, 10)
        with self.assertRaises(ValueError):
            area_triangulo_escaleno(1, 2, 3)  


class TestPerimetroTriangulo(unittest.TestCase):

    def test_perimetro(self):
        self.assertAlmostEqual(calcularPerimetro(0, 0, 4, 0, 0, 3), 12.0, places=3)

    def test_puntos_colineales(self):
        with self.assertRaises(ValueError):
            calcularPerimetro(0, 0, 1, 1, 2, 2)

    def test_puntos_repetidos(self):
        with self.assertRaises(ValueError):
            calcularPerimetro(0, 0, 0, 0, 3, 4)


class TestClasificacionTriangulos(unittest.TestCase):

    def test_por_lados(self):
        self.assertEqual(clasificar_por_lados(3, 3, 3), "equilátero")
        self.assertEqual(clasificar_por_lados(3, 3, 5), "isósceles")
        self.assertEqual(clasificar_por_lados(3, 4, 5), "escaleno")

    def test_por_lados_invalidos(self):
        with self.assertRaises(ValueError):
            clasificar_por_lados(1, 2, 10)
        with self.assertRaises(ValueError):
            clasificar_por_lados(0, 2, 2)

    def test_por_angulos(self):
        self.assertEqual(clasificar_por_angulos(90, 45, 45), "rectángulo")
        self.assertEqual(clasificar_por_angulos(60, 60, 60), "acutángulo")
        self.assertEqual(clasificar_por_angulos(120, 30, 30), "obtusángulo")

    def test_por_angulos_invalidos(self):
        with self.assertRaises(ValueError):
            clasificar_por_angulos(90, 45, 50) 
        with self.assertRaises(ValueError):
            clasificar_por_angulos(0, 90, 90)


class TestTriangulosNotablesYAproximados(unittest.TestCase):

    def test_notable_30(self):
        opuesto, adyacente, hipotenusa = triangulo_notable(30, 2, "opuesto")
        self.assertAlmostEqual(opuesto, 2)
        self.assertAlmostEqual(adyacente, 2 * math.sqrt(3))
        self.assertAlmostEqual(hipotenusa, 4)

    def test_notable_45_desde_hipotenusa(self):
        opuesto, adyacente, hipotenusa = triangulo_notable(45, math.sqrt(2), "hipotenusa")
        self.assertAlmostEqual(opuesto, 1)
        self.assertAlmostEqual(adyacente, 1)

    def test_notable_cumple_pitagoras(self):
        for angulo in (15, 30, 45, 60, 75):
            o, a, h = triangulo_notable(angulo, 3, "adyacente")
            self.assertAlmostEqual(o ** 2 + a ** 2, h ** 2)

    def test_notable_invalido(self):
        with self.assertRaises(ValueError):
            triangulo_notable(20, 2, "opuesto")      
        with self.assertRaises(ValueError):
            triangulo_notable(30, -2, "opuesto")     
        with self.assertRaises(ValueError):
            triangulo_notable(30, 2, "cateto")   

    def test_aproximado_37(self):
        self.assertEqual(triangulo_aproximado(37, 5, "hipotenusa"), (3, 4, 5))

    def test_aproximado_53(self):
        opuesto, adyacente, hipotenusa = triangulo_aproximado(53, 6, "adyacente")
        self.assertAlmostEqual(opuesto, 8)
        self.assertAlmostEqual(hipotenusa, 10)

    def test_aproximado_invalido(self):
        with self.assertRaises(ValueError):
            triangulo_aproximado(30, 5, "hipotenusa")
        with self.assertRaises(ValueError):
            triangulo_aproximado(37, 0, "hipotenusa")
        with self.assertRaises(ValueError):
            triangulo_aproximado(37, 5, "lado")


class TestCongruencia(unittest.TestCase):

    def test_lll(self):
        self.assertTrue(congruencia_lll((3, 4, 5), (5, 3, 4)))
        self.assertFalse(congruencia_lll((3, 4, 5), (3, 4, 6)))
        with self.assertRaises(ValueError):
            congruencia_lll((1, 2, 10), (3, 4, 5))

    def test_lal(self):
        self.assertTrue(congruencia_lal((3, 60, 4), (4, 60, 3)))
        self.assertFalse(congruencia_lal((3, 60, 4), (3, 70, 4)))
        with self.assertRaises(ValueError):
            congruencia_lal((3, 180, 4), (3, 60, 4))

    def test_ala(self):
        self.assertTrue(congruencia_ala((40, 5, 60), (60, 5, 40)))
        self.assertFalse(congruencia_ala((40, 5, 60), (40, 5, 70)))
        with self.assertRaises(ValueError):
            congruencia_ala((100, 5, 90), (40, 5, 60)) 

    def test_lla(self):
        self.assertTrue(congruencia_lla((5, 4, 50), (5, 4, 50)))
        self.assertFalse(congruencia_lla((5, 4, 50), (5, 4, 60)))

    def test_lla_caso_ambiguo(self):
        with self.assertRaises(ValueError):
            congruencia_lla((3, 5, 30), (3, 5, 30)) 

    def test_lla_lados_iguales_angulo_obtuso(self):
        with self.assertRaises(ValueError):
            congruencia_lla((4, 4, 100), (4, 4, 100))


class TestTeoremaCoseno(unittest.TestCase):

    def test_angulo_recto(self):
        self.assertAlmostEqual(teorema_coseno(3, 4, 90), 5)

    def test_angulo_60(self):
        self.assertAlmostEqual(teorema_coseno(1, 1, 60), 1)

    def test_invalidos(self):
        with self.assertRaises(ValueError):
            teorema_coseno(0, 4, 90)
        with self.assertRaises(ValueError):
            teorema_coseno(3, 4, 180)


class TestGraficosTriangulos(unittest.TestCase):

    def tearDown(self):
        plt.close("all")

    def test_graficos_validos(self):
        graphic.graficar_triangulo(0, 0, 4, 0, 0, 3)
        graphic.graficar_notable(30, 5, "hipotenusa")
        graphic.graficar_aproximado(37, 3, "opuesto")
        for t1, t2, criterio in (((3, 4, 5), (5, 3, 4), "LLL"),
                                 ((3, 60, 4), (4, 60, 3), "LAL"),
                                 ((40, 5, 60), (40, 5, 70), "ALA"),
                                 ((5, 4, 50), (5, 4, 50), "LLA")):
            graphic.graficar_congruencia(t1, t2, criterio)

    def test_vertices_lll_respetan_los_lados(self):
        A, B, C = graphic._vertices_desde_criterio((3, 4, 5), "LLL")
        self.assertAlmostEqual(math.dist(B, C), 3)
        self.assertAlmostEqual(math.dist(A, C), 4)
        self.assertAlmostEqual(math.dist(A, B), 5)

    def test_graficos_invalidos(self):
        with self.assertRaises(ValueError):
            graphic.graficar_triangulo(0, 0, 1, 1, 2, 2)
        with self.assertRaises(ValueError):
            graphic.graficar_congruencia((3, 4, 5), (3, 4, 5), "XYZ")
        with self.assertRaises(ValueError):
            graphic.graficar_congruencia((1, 2, 10), (3, 4, 5), "LLL")


if __name__ == "__main__":
    unittest.main()