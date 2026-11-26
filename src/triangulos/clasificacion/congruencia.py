from validaciones import validar_lados, iguales

def clasificar_por_lados(a, b, c):
    '''
    Se reciben las longitudes de los tres lados de un triángulo.
    a, b, c: longitudes de los lados

    Regla: equilátero  -> los tres lados son iguales
           isósceles   -> exactamente dos lados son iguales
           escaleno    -> los tres lados son distintos

    Se lanza ValueError si algún lado es menor o igual a 0, o si los lados
    no cumplen la desigualdad triangular (a + b > c, a + c > b, b + c > a).

    Se retorna "equilátero", "isósceles" o "escaleno".
    '''
    validar_lados(a, b, c)
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError(f"Los lados ({a}, {b}, {c}) no cumplen la desigualdad triangular.")

    if iguales(a, b) and iguales(b, c):
        return "equilátero"
    if iguales(a, b) or iguales(b, c) or iguales(a, c):
        return "isósceles"
    return "escaleno"