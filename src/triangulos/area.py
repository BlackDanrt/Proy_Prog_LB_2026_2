from math import sqrt

def area_triangulo(b, h):
    '''
    Se recibe la base y la altura de un triángulo.
    b: longitud de la base
    h: altura (distancia perpendicular desde la base hasta el vértice opuesto)
 
    Formula: Área = (b * h) / 2
 
    Se retorna el área del triángulo.
    '''
    return (b * h) / 2
 

def area_triangulo_equilatero(l):
    '''
    Se recibe la longitud del lado de un triángulo equilátero.
    l: longitud del lado
 
    Formula: Área = (sqrt(3) / 4) * l * l
 
    Se retorna el área del triángulo equilátero.
    '''
    return round((sqrt(3) / 4) * l * l, 3)
 
 
def area_triangulo_isosceles(b, h):
    '''
    Se recibe la base y la altura de un triángulo isósceles.
    b: longitud de la base (lado diferente)
    h: altura (distancia perpendicular desde la base hasta el vértice opuesto)
 
    Formula: Área = (b * h) / 2
 
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
 	
 	Se retorna el área del triángulo escaleno.
    '''
    s = (a + b + c) / 2
    return round(sqrt(s * (s - a) * (s - b) * (s - c)), 3)
 
def area_triangulo_rectangulo(cateto1, cateto2):
    '''
    Se recibe los dos catetos de un triángulo rectángulo.
    cateto1: longitud del primer cateto
    cateto2: longitud del segundo cateto
 
    Formula: Area = (cateto1 * cateto2) / 2
 
    Se retorna el área del triángulo rectángulo.
    '''
    return (cateto1 * cateto2) / 2
 
 
def area_triangulo_acutangulo(b, h):
    '''
    Se recibe la base y la altura de un triángulo acutángulo.
    b: longitud de la base
    h: altura
 
    Formula: Area = (b * h) / 2
 
    Se retorna el área del triángulo acutángulo.
    '''
    return area_triangulo(b, h)
 
 
def area_triangulo_obtusangulo(b, h):
    '''
    Se recibe la base y la altura de un triángulo obtusángulo.
    b: longitud de la base
    h: altura 
 
    Formula: Área = (b * h) / 2
 
    Se retorna el área del triángulo obtusángulo.
    '''
    return area_triangulo(b, h)
