import math


def validar_lados(*lados):
    '''
    Se reciben una o más longitudes de lados.

    Se lanza ValueError si algún lado es menor o igual a 0.
    '''
    for lado in lados:
        if lado <= 0:
            raise ValueError(f"Los lados deben ser mayores que 0 (se recibió {lado}).")


def validar_angulo(angulo):
    '''
    Se recibe un ángulo en grados.

    Se lanza ValueError si el ángulo no está estrictamente entre 0 y 180 grados.
    '''
    if angulo <= 0 or angulo >= 180:
        raise ValueError(f"El ángulo debe estar entre 0 y 180 grados (se recibió {angulo}).")

def validar_radios(*radios):
    '''
    Se reciben uno o más radios.

    Se lanza ValueError si algún radio es menor o igual a 0.
    '''
    for radio in radios:
        if radio <= 0:
            raise ValueError(f"Los radios deben ser mayores que 0 (se recibió {radio}).")
            
def iguales(x, y):
    '''
    Se reciben dos números.

    Se retorna True si son iguales con una tolerancia pequeña,
    para evitar errores de redondeo con números decimales.
    '''
    return math.isclose(x, y, rel_tol=1e-9, abs_tol=1e-9)


def validar_numero_lados(n):
    '''
    Se recibe el número de lados de un polígono.
    n: número de lados (entero)

    Se lanza ValueError si n no es un entero o si es menor que 3.
    '''
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"El número de lados debe ser un entero (se recibió {n!r}).")
    if n < 3:
        raise ValueError(f"Un polígono debe tener al menos 3 lados (se recibió {n}).")


def producto_cruz(o, a, b):
    '''
    Se reciben tres puntos (x, y).
    o: punto de origen
    a: primer punto
    b: segundo punto

    Formula: (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

    Se retorna un valor positivo si o -> a -> b gira a la izquierda,
    negativo si gira a la derecha y 0 si los tres puntos son colineales.
    '''
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def _sobre_segmento(p, q, r):
    '''
    Se reciben los extremos de un segmento (p, q) y un punto r colineal con ellos.

    Se retorna True si r está dentro del segmento p-q, False en caso contrario.
    '''
    return (min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and
            min(p[1], q[1]) <= r[1] <= max(p[1], q[1]))


def _segmentos_se_cruzan(p1, p2, p3, p4):
    '''
    Se reciben los extremos de dos segmentos: p1-p2 y p3-p4.

    Se retorna True si los segmentos se cortan o se tocan, False en caso contrario.
    '''
    d1 = producto_cruz(p3, p4, p1)
    d2 = producto_cruz(p3, p4, p2)
    d3 = producto_cruz(p1, p2, p3)
    d4 = producto_cruz(p1, p2, p4)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
       ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True

    # Casos colineales: un extremo está sobre el otro segmento
    if iguales(d1, 0) and _sobre_segmento(p3, p4, p1):
        return True
    if iguales(d2, 0) and _sobre_segmento(p3, p4, p2):
        return True
    if iguales(d3, 0) and _sobre_segmento(p1, p2, p3):
        return True
    if iguales(d4, 0) and _sobre_segmento(p1, p2, p4):
        return True
    return False


def validar_poligono(vertices):
    '''
    Se recibe la lista de vértices de un polígono, en orden (horario o antihorario).
    vertices: lista de tuplas (x, y), por ejemplo [(0, 0), (4, 0), (4, 3)]

    Se lanza ValueError si:
        - hay menos de 3 vértices
        - algún vértice no es una tupla (x, y) de números
        - hay vértices repetidos
        - hay tres vértices consecutivos colineales
        - dos lados no consecutivos se cruzan (el polígono no es simple)
    '''
    if not isinstance(vertices, (list, tuple)) or len(vertices) < 3:
        raise ValueError("Un polígono necesita al menos 3 vértices.")

    for v in vertices:
        if not isinstance(v, (list, tuple)) or len(v) != 2:
            raise ValueError(f"Cada vértice debe ser una tupla (x, y) (se recibió {v!r}).")
        for c in v:
            if isinstance(c, bool) or not isinstance(c, (int, float)):
                raise ValueError(f"Las coordenadas deben ser números (se recibió {v!r}).")

    n = len(vertices)

    for i in range(n):
        for j in range(i + 1, n):
            if iguales(vertices[i][0], vertices[j][0]) and iguales(vertices[i][1], vertices[j][1]):
                raise ValueError(f"El vértice {vertices[i]} está repetido.")

    for i in range(n):
        anterior, actual, siguiente = vertices[i - 1], vertices[i], vertices[(i + 1) % n]
        if iguales(producto_cruz(anterior, actual, siguiente), 0):
            raise ValueError(f"Los vértices {anterior}, {actual} y {siguiente} son colineales.")

    for i in range(n):
        for j in range(i + 1, n):
            # Se saltan los lados consecutivos (comparten un vértice)
            if j == i + 1 or (i == 0 and j == n - 1):
                continue
            if _segmentos_se_cruzan(vertices[i], vertices[(i + 1) % n],
                                    vertices[j], vertices[(j + 1) % n]):
                raise ValueError("Los lados del polígono se cruzan; el polígono no es simple.")