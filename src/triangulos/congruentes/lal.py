from validaciones import validar_lados, validar_angulo, iguales

def congruencia_lal(t1, t2):
    '''
    Criterio L-A-L (lado - ángulo - lado).
    Se reciben dos triángulos, cada uno como una tupla con dos lados y el
    ángulo comprendido entre ellos.
    t1: (a, gamma, b) primer triángulo
    t2: (a, gamma, b) segundo triángulo
    a, b: longitudes de dos lados
    gamma: ángulo (en grados) formado entre los lados a y b

    Regla: dos triángulos son congruentes si tienen dos lados iguales y el
    ángulo comprendido entre ellos también es igual.

    Se lanza ValueError si algún lado es menor o igual a 0, o si el ángulo
    no está estrictamente entre 0 y 180 grados.

    Se retorna True si los triángulos son congruentes, False si no.
    '''
    for a, gamma, b in (t1, t2):
        validar_lados(a, b)
        validar_angulo(gamma)

    a1, g1, b1 = t1
    a2, g2, b2 = t2
    ladosiguales = (iguales(a1, a2) and iguales(b1, b2)) or \
                    (iguales(a1, b2) and iguales(b1, a2))
    return ladosiguales and iguales(g1, g2)