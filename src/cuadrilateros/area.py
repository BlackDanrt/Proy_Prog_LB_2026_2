from validaciones import validar_lados


def area_trapecio(b1, b2, h):
    '''
    Se recibe las dos bases paralelas y la altura del trapecio.
    b1: longitud de la base mayor
    b2: longitud de la base menor
    h : altura (distancia perpendicular entre las dos bases)

    Formula: Área = ((b1 + b2) / 2) * h

    Se lanza ValueError si alguna base o la altura son menores o iguales a 0,
    o si las dos bases son iguales (en ese caso sería un paralelogramo).

    Se retorna el área del trapecio.
    '''
    validar_lados(b1, b2, h)
    if b1 == b2:
        raise ValueError("Las bases de un trapecio deben ser distintas; si son iguales es un paralelogramo.")
    return ((b1 + b2) / 2) * h


def area_trapecio_rectangulo(b1, b2, h):
    '''
    Se recibe las dos bases paralelas y la altura del trapecio.

    Se llama a la función que calcula el area de un trapecio.

    Se lanza ValueError en los mismos casos que area_trapecio.

    Se retorna el área del trapecio rectangulo.
    '''
    return area_trapecio(b1, b2, h)


def area_trapecio_isosceles(b1, b2, h):
    '''
    Se recibe las dos bases paralelas y la altura del trapecio.

    Se llama a la función que calcula el area de un trapecio.

    Se lanza ValueError en los mismos casos que area_trapecio.

    Se retorna el área del trapecio isosceles.
    '''
    return area_trapecio(b1, b2, h)


def area_trapecio_escaleno(b1, b2, h):
    '''
    Se recibe las dos bases paralelas y la altura del trapecio.

    Se llama a la función que calcula el area de un trapecio.

    Se lanza ValueError en los mismos casos que area_trapecio.

    Se retorna el área del trapecio escaleno.
    '''
    return area_trapecio(b1, b2, h)


def area_paralelogramo(b, h):
    '''
    Se recibe la base y la altura de un paralelogramo.
    b: longitud de la base
    h: altura (distancia perpendicular a la base)

    Formula: Área = b * h

    Se lanza ValueError si la base o la altura son menores o iguales a 0.

    Se retorna el área del paralelogramo.
    '''
    validar_lados(b, h)
    return b * h


def area_romboide(b, h):
    '''
    La función recibe la base y la altura de un romboide.
    b: longitud de la base
    h: altura (distancia perpendicular a la base)

    Formula: Área = b * h

    Se lanza ValueError si la base o la altura son menores o iguales a 0.

    Se retorna el área del romboide.
    '''
    return area_paralelogramo(b, h)


def area_rombo(d1, d2):
    '''
    La función recibe las dos diagonales de un rombo.
    d1: longitud de la diagonal mayor
    d2: longitud de la diagonal menor

    Formula: Área = (d1 * d2) / 2

    Se lanza ValueError si alguna diagonal es menor o igual a 0.

    Se retorna el área del rombo.
    '''
    validar_lados(d1, d2)
    return (d1 * d2) / 2


def area_rectangulo(l, w):
    '''
    La función recibe el largo y el ancho de un rectángulo.
    l: largo del rectángulo
    w: ancho del rectángulo

    Formula: Área = l * w

    Se lanza ValueError si el largo o el ancho son menores o iguales a 0.

    Se retorna el área del rectangulo.
    '''
    validar_lados(l, w)
    return l * w


def area_cuadrado(l):
    '''
    La función recibe la longitud del lado de un cuadrado.
    l: longitud del lado

    Formula: Área = l * l

    Se lanza ValueError si el lado es menor o igual a 0.

    Se retorna el área del cuadrado.
    '''
    validar_lados(l)
    return l ** 2