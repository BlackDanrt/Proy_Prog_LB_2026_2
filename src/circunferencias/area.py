from math import pi
from validaciones import validar_radios


def calcularArea(radio):
    '''
    Se recibe el radio de una circunferencia.
    radio: radio de la circunferencia

    Formula: Área = pi * radio * radio

    Se lanza ValueError si el radio es menor o igual a 0.

    Se retorna el área de la circunferencia con 3 decimales.
    '''
    validar_radios(radio)
    return round(pi * (radio ** 2), 3)