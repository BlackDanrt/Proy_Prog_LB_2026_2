from math import sqrt


def calcularPerimetro(x1, y1, x2, y2, x3, y3):
    '''
    Se recibe como parametro 6 variables que corresponden a los 3 puntos (x,y) que conforman un triángulo.

    Se calcula la distancia de un punto a un punto b en sentido horario.

    Se lanza ValueError si los tres puntos están sobre una misma recta
    (incluye el caso de puntos repetidos), porque así no forman un triángulo.

    Se retorna el perimetro con una precisión de 3 decimales.
    '''
    # Si el área (producto cruz) es 0, los puntos son colineales
    producto_cruz = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if abs(producto_cruz) < 1e-9:
        raise ValueError(
            f"Los puntos ({x1}, {y1}), ({x2}, {y2}) y ({x3}, {y3}) son colineales "
            "o están repetidos; no forman un triángulo."
        )

    perimetro = 0
    perimetro += sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    perimetro += sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    perimetro += sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    return round(perimetro, 3)