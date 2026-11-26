from math import sqrt, atan2, degrees
from validaciones import iguales, validar_poligono, producto_cruz
from poligonos.clasificacion.clasificacion_poligonos import clasificar_por_forma
def _longitudes_lados(vertices):
    '''
    Se recibe la lista de vértices de un polígono, en orden.

    Se retorna una lista con la longitud de cada lado.
    '''
    n = len(vertices)
    lados = []
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        lados.append(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    return lados


def _angulos_interiores(vertices):
    '''
    Se recibe la lista de vértices de un polígono convexo, en orden.

    Formula: en cada vértice se toman los vectores hacia el vértice anterior (u)
    y hacia el siguiente (v):
        ángulo = atan2(|u x v|, u · v)

    Se retorna una lista con el ángulo interior (en grados) de cada vértice.
    '''
    n = len(vertices)
    angulos = []
    for i in range(n):
        anterior, actual, siguiente = vertices[i - 1], vertices[i], vertices[(i + 1) % n]
        ux, uy = anterior[0] - actual[0], anterior[1] - actual[1]
        vx, vy = siguiente[0] - actual[0], siguiente[1] - actual[1]
        cruz = abs(producto_cruz(actual, anterior, siguiente))
        punto = ux * vx + uy * vy
        angulos.append(degrees(atan2(cruz, punto)))
    return angulos


def es_equilatero(vertices):
    '''
    Se recibe la lista de vértices de un polígono, en orden.
    vertices: lista de tuplas (x, y)

    Un polígono es equilátero si todos sus lados miden lo mismo.

    Se lanza ValueError si los vértices no forman un polígono simple válido
    (ver validar_poligono).

    Se retorna True si el polígono es equilátero, False en caso contrario.
    '''
    validar_poligono(vertices)
    lados = _longitudes_lados(vertices)
    return all(iguales(lado, lados[0]) for lado in lados)


def es_equiangulo(vertices):
    '''
    Se recibe la lista de vértices de un polígono, en orden.
    vertices: lista de tuplas (x, y)

    Un polígono es equiángulo si todos sus ángulos interiores miden lo mismo.
    En ese caso cada ángulo vale (n - 2) * 180 / n, que siempre es menor que
    180°, por lo que un polígono cóncavo nunca es equiángulo.

    Se lanza ValueError si los vértices no forman un polígono simple válido
    (ver validar_poligono).

    Se retorna True si el polígono es equiángulo, False en caso contrario.
    '''
    validar_poligono(vertices)
    if clasificar_por_forma(vertices) == "cóncavo":
        return False
    angulos = _angulos_interiores(vertices)
    return all(iguales(angulo, angulos[0]) for angulo in angulos)
