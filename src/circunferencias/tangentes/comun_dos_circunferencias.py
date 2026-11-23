from math import sqrt
from validaciones import validar_lados, iguales

def tangente_comun_exterior(r1, r2, d):
    '''
    Se reciben los radios de dos circunferencias y la distancia entre sus centros.
    r1: radio de la primera circunferencia
    r2: radio de la segunda circunferencia
    d: distancia entre los centros

    Formula: L = sqrt(d² - (r1 - r2)²)
             (la tangente exterior deja ambas circunferencias del mismo lado)

    Se lanza ValueError si algún radio es menor o igual a 0, si d es negativa,
    si las circunferencias son la misma (d = 0 y r1 = r2), o si
    d < |r1 - r2| (una circunferencia está dentro de la otra y no hay
    tangente común).

    Se retorna la longitud de la tangente común exterior con 3 decimales.
    '''
    validar_lados(r1, r2)
    if d < 0:
        raise ValueError(f"La distancia entre centros no puede ser negativa (se recibió {d}).")
    if iguales(d, 0) and iguales(r1, r2):
        raise ValueError("Las dos circunferencias son la misma; tienen infinitas tangentes comunes.")
    if d < abs(r1 - r2):
        raise ValueError(
            f"Una circunferencia está dentro de la otra (d = {d} < |r1 - r2| = {abs(r1 - r2)}); "
            "no hay tangente común."
        )
    return round(sqrt(d ** 2 - (r1 - r2) ** 2), 3)


def tangente_comun_interior(r1, r2, d):
    '''
    Se reciben los radios de dos circunferencias y la distancia entre sus centros.
    r1: radio de la primera circunferencia
    r2: radio de la segunda circunferencia
    d: distancia entre los centros

    Formula: L = sqrt(d² - (r1 + r2)²)
             (la tangente interior pasa entre las dos circunferencias)

    Se lanza ValueError si algún radio es menor o igual a 0, si d es negativa,
    o si d < r1 + r2 (las circunferencias se cortan o una está dentro de la
    otra, y no hay tangente común interior).

    Se retorna la longitud de la tangente común interior con 3 decimales
    (0 si las circunferencias son tangentes exteriores).
    '''
    validar_lados(r1, r2)
    if d < 0:
        raise ValueError(f"La distancia entre centros no puede ser negativa (se recibió {d}).")
    if d < r1 + r2:
        raise ValueError(
            f"Las circunferencias se cortan o una está dentro de la otra "
            f"(d = {d} < r1 + r2 = {r1 + r2}); no hay tangente común interior."
        )
    return round(sqrt(d ** 2 - (r1 + r2) ** 2), 3)