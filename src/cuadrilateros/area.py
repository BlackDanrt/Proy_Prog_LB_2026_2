def area_trapecio(b1, b2, h):
    '''
    Se recibe las dos bases paralelas y la altura del trapecio.
    b1: longitud de la base mayor
    b2: longitud de la base menor
    h : altura (distancia perpendicular entre las dos bases)
 
    Formula: Área = ((b1 + b2) / 2) * h
 
    Se retorna el área del trapecio.
    '''
    return ((b1 + b2) / 2) * h
 
def area_trapecio_rectangulo(b1, b2, h):
    '''
    Se recibe las dos bases paralelas y la altura del trapecio.
    
    Se llama a la función que calcula el area de un trapecio.

    Se retorna el área del trapecio rectangulo.
    '''
    return area_trapecio(b1, b2, h)
 
def area_trapecio_isosceles(b1, b2, h):
    '''
    Se recibe las dos bases paralelas y la altura del trapecio.
    
    Se llama a la función que calcula el area de un trapecio.
    
    Se retorna el área del trapecio isosceles.
    '''
    return area_trapecio(b1, b2, h)
 
def area_trapecio_escaleno(b1, b2, h):
    '''
    Se recibe las dos bases paralelas y la altura del trapecio.
    
    Se llama a la función que calcula el area de un trapecio.
    
    Se retorna el área del trapecio escaleno.
    '''
    return area_trapecio(b1, b2, h)
 
def area_paralelogramo(b, h):
    '''
    Se recibe la base y la altura de un paralelogramo.
    b: longitud de la base
    h: altura (distancia perpendicular a la base)
 
    Formula: Área = b * h
 
    Se retorna el área del paralelogramo.
    '''
    return b * h
 
def area_romboide(b, h):
    '''
    La función recibe la base y la altura de un romboide.
    b: longitud de la base
    h: altura (distancia perpendicular a la base)
 
    Formula: Área = b * h
 
    Se retorna el área del romboide.
    '''
    return area_paralelogramo(b, h)
 
def area_rombo(d1, d2):
    '''
    La función recibe las dos diagonales de un rombo.
    d1: longitud de la diagonal mayor
    d2: longitud de la diagonal menor
 
    Formula: Área = (d1 * d2) / 2
 
    Se retorna el área del rombo.
    '''
    return (d1 * d2) / 2
 
def area_rectangulo(l, w):
    '''
    La función recibe el largo y el ancho de un rectángulo.
    l: largo del rectángulo
    w: ancho del rectángulo
 
    Formula: Área = l * w
 
    Se retorna el área del rectangulo.
    '''
    return l * w
 
def area_cuadrado(l):
    '''
    La función recibe la longitud del lado de un cuadrado.
    l: longitud del lado
 
    Formula: Área = l * l
 
    Se retorna el área del cuadrado.
    '''
    return l ** 2