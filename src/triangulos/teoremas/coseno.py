import math

def teorema_coseno(a, b, gamma):
    '''
    Se reciben dos lados de un triángulo y el ángulo comprendido entre ellos.
    a: longitud del primer lado
    b: longitud del segundo lado
    gamma: ángulo (en grados) formado entre los lados a y b

    Formula: c² = a² + b² - 2 * a * b * cos(gamma)

    Se lanza ValueError si algún lado es menor o igual a 0,
    o si el ángulo no está estrictamente entre 0 y 180 grados.

    Se retorna la longitud del lado c, opuesto al ángulo gamma.
    '''
    if a <= 0 or b <= 0:
        raise ValueError("Los lados del triángulo deben ser mayores que 0.")
    if gamma <= 0 or gamma >= 180:
        raise ValueError("El ángulo debe estar entre 0 y 180 grados (sin incluirlos).")

    return math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(gamma)))
