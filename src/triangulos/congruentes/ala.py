from validaciones import validar_lados, validar_angulo, iguales

def congruencia_ala(t1, t2):
    '''
    Criterio A-L-A (ángulo - lado - ángulo).
    Se reciben dos triángulos, cada uno como una tupla con dos ángulos y el
    lado comprendido entre ellos.
    t1: (alfa, c, beta) primer triángulo
    t2: (alfa, c, beta) segundo triángulo
    alfa, beta: ángulos (en grados) en los extremos del lado c
    c: longitud del lado comprendido entre los dos ángulos

    Regla: dos triángulos son congruentes si tienen dos ángulos iguales y el
    lado comprendido entre ellos también es igual.

    Se lanza ValueError si el lado es menor o igual a 0, si algún ángulo no
    está entre 0 y 180 grados, o si la suma de los dos ángulos es mayor o
    igual a 180 grados (no se podría formar el triángulo).

    Se retorna True si los triángulos son congruentes, False si no.
    '''
    for alfa, c, beta in (t1, t2):
        validar_lados(c)
        validar_angulo(alfa)
        validar_angulo(beta)
        if alfa + beta >= 180:
            raise ValueError(f"La suma de los ángulos {alfa} + {beta} debe ser menor que 180.")

    al1, c1, be1 = t1
    al2, c2, be2 = t2
    angulosiguales = (iguales(al1, al2) and iguales(be1, be2)) or \
                      (iguales(al1, be2) and iguales(be1, al2))
    return angulosiguales and iguales(c1, c2)