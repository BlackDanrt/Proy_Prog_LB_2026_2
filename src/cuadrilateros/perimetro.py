from math import sqrt

def _orientacion(ax, ay, bx, by, cx, cy):
    '''
    Se reciben tres puntos a, b y c.

    Formula: producto cruz (b - a) x (c - a)

    Se retorna un número positivo si el giro a -> b -> c es antihorario,
    negativo si es horario y 0 si los tres puntos son colineales.
    '''
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)


def _segmentos_se_cruzan(p1, p2, p3, p4):
    '''
    Se reciben los extremos de dos segmentos: p1-p2 y p3-p4.

    Se retorna True si los segmentos se cruzan en un punto interior.
    '''
    d1 = _orientacion(*p3, *p4, *p1)
    d2 = _orientacion(*p3, *p4, *p2)
    d3 = _orientacion(*p1, *p2, *p3)
    d4 = _orientacion(*p1, *p2, *p4)
    return d1 * d2 < 0 and d3 * d4 < 0


def calcularPerimetro(x1, y1, x2, y2, x3, y3, x4, y4):
    '''
    Se recibe como parametro 8 variables que corresponden a los 4 puntos (x,y) que conforman un cuadrilatero

    Se calcula la distancia de un punto a un punto b en sentido horario

    Se lanza ValueError si tres puntos consecutivos están sobre una misma
    recta (incluye puntos repetidos), o si dos lados opuestos se cruzan
    (los puntos no están en orden y forman un "moño", no un cuadrilátero).

    Se retorna el perimetro con una precisión de 3 decimales
    '''
    puntos = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

    for i in range(4):
        a, b, c = puntos[i], puntos[(i + 1) % 4], puntos[(i + 2) % 4]
        if abs(_orientacion(*a, *b, *c)) < 1e-9:
            raise ValueError(
                f"Los puntos {a}, {b} y {c} son colineales o están repetidos; "
                "no forman un cuadrilátero."
            )

    if _segmentos_se_cruzan(puntos[0], puntos[1], puntos[2], puntos[3]) or \
       _segmentos_se_cruzan(puntos[1], puntos[2], puntos[3], puntos[0]):
        raise ValueError(
            "Dos lados opuestos se cruzan; los puntos deben darse en orden "
            "(horario o antihorario) alrededor del cuadrilátero."
        )

    perimetro = 0
    perimetro += sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    perimetro += sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    perimetro += sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
    perimetro += sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
    return round(perimetro, 3)