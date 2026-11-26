from math import tan, pi
from validaciones import validar_lados, validar_poligono, validar_numero_lados


def area_poligono(vertices):
    '''
    Se recibe la lista de vértices de un polígono, en orden (horario o antihorario).
    vertices: lista de tuplas (x, y)

    Formula (fórmula del área de Gauss o "de los cordones"):
        Área = |Σ (x_i * y_(i+1) - x_(i+1) * y_i)| / 2
        donde el vértice siguiente al último es el primero.

    Sirve para cualquier polígono simple, cóncavo o convexo.

    Se lanza ValueError si los vértices no forman un polígono simple válido
    (ver validar_poligono).

    Se retorna el área del polígono.
    '''
    validar_poligono(vertices)
    n = len(vertices)
    suma = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        suma += x1 * y2 - x2 * y1
    return round(abs(suma) / 2, 3)


def area_poligono_regular(n, l):
    '''
    Se recibe el número de lados y la longitud del lado de un polígono regular.
    n: número de lados (entero mayor o igual a 3)
    l: longitud del lado

    Formula: Área = (n * l * l) / (4 * tan(π / n))

    Se lanza ValueError si n no es un entero mayor o igual a 3, o si el lado
    es menor o igual a 0.

    Se retorna el área del polígono regular.
    '''
    validar_numero_lados(n)
    validar_lados(l)
    return round((n * l * l) / (4 * tan(pi / n)), 3)


def area_poligono_regular_apotema(n, l, apotema):
    '''
    Se recibe el número de lados, la longitud del lado y la apotema de un polígono regular.
    n: número de lados (entero mayor o igual a 3)
    l: longitud del lado
    apotema: distancia perpendicular desde el centro hasta un lado

    Formula: Área = (perímetro * apotema) / 2 = (n * l * apotema) / 2

    Se lanza ValueError si n no es un entero mayor o igual a 3, o si el lado
    o la apotema son menores o iguales a 0.

    Se retorna el área del polígono regular.
    '''
    validar_numero_lados(n)
    validar_lados(l, apotema)
    return round((n * l * apotema) / 2, 3)