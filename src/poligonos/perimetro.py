from math import sqrt
from validaciones import validar_lados, validar_poligono, validar_numero_lados


def calcularPerimetro(vertices):
    '''
    Se recibe la lista de vértices de un polígono, en orden.
    vertices: lista de tuplas (x, y)

    Formula:
        lado_i = sqrt((x_(i+1) - x_i)² + (y_(i+1) - y_i)²)
        Perímetro = Σ lado_i
        donde el vértice siguiente al último es el primero.

    Se lanza ValueError si los vértices no forman un polígono simple válido
    (ver validar_poligono).

    Se retorna el perímetro del polígono.
    '''
    validar_poligono(vertices)
    n = len(vertices)
    perimetro = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        perimetro += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(perimetro, 3)


def perimetro_poligono_regular(n, l):
    '''
    Se recibe el número de lados y la longitud del lado de un polígono regular.
    n: número de lados (entero mayor o igual a 3)
    l: longitud del lado

    Formula: Perímetro = n * l

    Se lanza ValueError si n no es un entero mayor o igual a 3, o si el lado
    es menor o igual a 0.

    Se retorna el perímetro del polígono regular.
    '''
    validar_numero_lados(n)
    validar_lados(l)
    return n * l