from math import sqrt

def calcularPerimetro(x1,y1, x2,y2, x3, y3):
    '''
    Se recibe como parametro 6 variables que corresponden a los 3 puntos (x,y) que conforman un triángulo.

    Se calcula la distancia de un punto a un punto b en sentido horario.

    Se retorna el perimetro con una precisión de 3 decimales.
    '''
    perimetro = 0
    perimetro += sqrt((((x1 - x2)))**2 + ((y1 - y2)**2))
    perimetro += sqrt((((x2 - x3)))**2 + ((y2 - y3)**2))
    perimetro += sqrt((((x3 - x1)))**2 + ((y3 - y1)**2))
    return round(perimetro,3)
