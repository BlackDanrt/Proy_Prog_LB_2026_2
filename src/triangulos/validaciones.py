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


def iguales(x, y):
    '''
    Se reciben dos números.

    Se retorna True si son iguales con una tolerancia pequeña,
    para evitar errores de redondeo con números decimales.
    '''
    return math.isclose(x, y, rel_tol=1e-9, abs_tol=1e-9)
