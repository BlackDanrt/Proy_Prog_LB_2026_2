import unittest

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from circunferencias.area import calcularArea
from circunferencias.tangentes.comun_dos_circunferencias import (
    tangente_comun_exterior,
    tangente_comun_interior,
)
from circunferencias import graphic


class TestAreaCircunferencia(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(calcularArea(1), 3.142, places=3)
        self.assertAlmostEqual(calcularArea(3), 28.274, places=3)

    def test_radio_invalido(self):
        with self.assertRaises(ValueError):
            calcularArea(0)
        with self.assertRaises(ValueError):
            calcularArea(-2)


class TestTangenteExterior(unittest.TestCase):

    def test_longitud(self):
        self.assertAlmostEqual(tangente_comun_exterior(3, 1.5, 7), 6.837, places=3)

    def test_radios_iguales(self):
        self.assertAlmostEqual(tangente_comun_exterior(2, 2, 5), 5, places=3)

    def test_una_dentro_de_otra(self):
        with self.assertRaises(ValueError):
            tangente_comun_exterior(5, 1, 2)

    def test_misma_circunferencia(self):
        with self.assertRaises(ValueError):
            tangente_comun_exterior(2, 2, 0)

    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            tangente_comun_exterior(0, 2, 5)
        with self.assertRaises(ValueError):
            tangente_comun_exterior(3, 2, -1)


class TestTangenteInterior(unittest.TestCase):

    def test_longitud(self):
        self.assertAlmostEqual(tangente_comun_interior(3, 1.5, 7), 5.362, places=3)

    def test_tangentes_exteriores(self):
        self.assertEqual(tangente_comun_interior(3, 2, 5), 0)

    def test_se_cortan(self):
        with self.assertRaises(ValueError):
            tangente_comun_interior(3, 3, 5)

    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            tangente_comun_interior(-1, 2, 5)
        with self.assertRaises(ValueError):
            tangente_comun_interior(3, 2, -10)


class TestGraficosCircunferencias(unittest.TestCase):

    def tearDown(self):
        plt.close("all")

    def test_graficos_validos(self):
        graphic.graficar_circunferencia(3)
        graphic.graficar_tangente_exterior(3, 1.5, 7)
        graphic.graficar_tangente_interior(3, 1.5, 7)

    def test_graficos_invalidos(self):
        with self.assertRaises(ValueError):
            graphic.graficar_circunferencia(0)
        with self.assertRaises(ValueError):
            graphic.graficar_tangente_exterior(5, 1, 2)
        with self.assertRaises(ValueError):
            graphic.graficar_tangente_interior(3, 3, 5)


if __name__ == "__main__":
    unittest.main()