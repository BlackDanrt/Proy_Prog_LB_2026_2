from math import sqrt
def calcularPerimetro(x1,y1, x2,y2, x3, y3, x4, y4):
    perimetro = 0
    perimetro += sqrt((((x1 - x2)))**2 + ((y1 - y2)**2))
    perimetro += sqrt((((x2 - x3)))**2 + ((y2 - y3)**2))
    perimetro += sqrt((((x3 - x4)))**2 + ((y3 - y4)**2))
    perimetro += sqrt((((x4 - x1)))**2 + ((y4 - y1)**2))
    return round(perimetro,3)
