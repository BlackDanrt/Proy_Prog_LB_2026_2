from math import pi
def calcularArea(radio):
    '''
    Se recibe el radio de una circunferencia.
    r: radio de la circunferencia
 
    Formula: Área = pi * r * r
 
    Se retorna el área de la circunferencia.
    '''
    return round(pi*(radio**2), 3)
