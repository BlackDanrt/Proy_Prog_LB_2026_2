from math import sqrt
from validaciones import validar_lados


def _validar_desigualdad_triangular(a, b, c):
    '''
    Se reciben los tres lados de un triángulo.

    Se lanza ValueError si no cumplen la desigualdad triangular
    (a + b > c, a + c > b, b + c > a).
    '''
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError(f"Los lados ({a}, {b}, {c}) no cumplen la desigualdad triangular.")


def area_triangulo(b, h):
    '''
    Se recibe la base y la altura de un triángulo.
    b: longitud de la base
    h: altura (distancia perpendicular desde la base hasta el vértice opuesto)

    Formula: Área = (b * h) / 2

    Se lanza ValueError si la base o la altura son menores o iguales a 0.

    Se retorna el área del triángulo.
    '''
    validar_lados(b, h)
    return (b * h) / 2


def area_triangulo_equilatero(l):
    '''
    Se recibe la longitud del lado de un triángulo equilátero.
    l: longitud del lado

    Formula: Área = (sqrt(3) / 4) * l * l

    Se lanza ValueError si el lado es menor o igual a 0.

    Se retorna el área del triángulo equilátero.
    '''
    validar_lados(l)
    return round((sqrt(3) / 4) * l * l, 3)


def area_triangulo_isosceles(b, h):
    '''
    Se recibe la base y la altura de un triángulo isósceles.
    b: longitud de la base (lado diferente)
    h: altura (distancia perpendicular desde la base hasta el vértice opuesto)

    Formula: Área = (b * h) / 2

    Se lanza ValueError si la base o la altura son menores o iguales a 0.

    Se retorna el área del triángulo isósceles.
    '''
    return area_triangulo(b, h)


def area_triangulo_escaleno(a, b, c):
    '''
    Se recibe los tres lados de un triángulo escaleno.
    a: longitud del primer lado
    b: longitud del segundo lado
    c: longitud del tercer lado

    Formula:
        s = (a + b + c) / 2
        Área = sqrt(s * (s-a) * (s-b) * (s-c))

    Se lanza ValueError si algún lado es menor o igual a 0, o si los lados
    no cumplen la desigualdad triangular.

    Se retorna el área del triángulo escaleno.
    '''
    validar_lados(a, b, c)
    _validar_desigualdad_triangular(a, b, c)
    s = (a + b + c) / 2
    return round(sqrt(s * (s - a) * (s - b) * (s - c)), 3)


def area_triangulo_rectangulo(cateto1, cateto2):
    '''
    Se recibe los dos catetos de un triángulo rectángulo.
    cateto1: longitud del primer cateto
    cateto2: longitud del segundo cateto

    Formula: Area = (cateto1 * cateto2) / 2

    Se lanza ValueError si algún cateto es menor o igual a 0.

    Se retorna el área del triángulo rectángulo.
    '''
    validar_lados(cateto1, cateto2)
    return (cateto1 * cateto2) / 2


def area_triangulo_acutangulo(b, h):
    '''
    Se recibe la base y la altura de un triángulo acutángulo.
    b: longitud de la base
    h: altura

    Formula: Area = (b * h) / 2

    Se lanza ValueError si la base o la altura son menores o iguales a 0.

    Se retorna el área del triángulo acutángulo.
    '''
    return area_triangulo(b, h)


def area_triangulo_obtusangulo(b, h):
    '''
    Se recibe la base y la altura de un triángulo obtusángulo.
    b: longitud de la base
    h: altura

    Formula: Área = (b * h) / 2

    Se lanza ValueError si la base o la altura son menores o iguales a 0.

    Se retorna el área del triángulo obtusángulo.
    '''
    return area_triangulo(b, h)