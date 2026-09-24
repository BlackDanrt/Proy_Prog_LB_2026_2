from math import sqrt
#La función recibe una lista de tuplas, en la cual cada tupla representan las coordenadas (x,y) del respectivo punto
#Ejemplo: puntos = [(0,0),(0,5),(7,1),(5,-4),(3,-2)]
def calcularPerimetro(puntos):
    perimetro = 0
    for i in range(len(puntos)):
        if i != (len(puntos)-1):
            perimetro += sqrt(((puntos[i][0] - puntos[(i+1)][0])**2) + ((puntos[i][1] - puntos[(i+1)][1])**2))
        else:
            perimetro += sqrt(((puntos[i][0] - puntos[0][0])**2) + ((puntos[i][1] - puntos[0][1])**2))
    return round(perimetro,3)
