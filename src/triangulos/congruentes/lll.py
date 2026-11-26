from validaciones import validar_lados, iguales

def congruencia_lll(t1, t2):
    '''
    Criterio L-L-L (lado - lado - lado).
    Se reciben dos triángulos, cada uno como una tupla con sus tres lados.
    t1: (a, b, c) lados del primer triángulo
    t2: (a, b, c) lados del segundo triángulo

    Regla: dos triángulos son congruentes si sus tres lados son
    respectivamente iguales.

    Se lanza ValueError si algún lado es menor o igual a 0, o si los lados
    no cumplen la desigualdad triangular (a + b > c, a + c > b, b + c > a).

    Se retorna True si los triángulos son congruentes, False si no.
    '''
    for t in (t1, t2):
        validar_lados(*t)
        a, b, c = t
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(f"Los lados {t} no cumplen la desigualdad triangular.")

    # Se ordenan los lados para comparar sin importar el orden en que se dieron
    return all(iguales(x, y) for x, y in zip(sorted(t1), sorted(t2)))
