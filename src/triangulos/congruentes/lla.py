from validaciones import validar_lados, validar_angulo, iguales

def congruencia_lla(t1, t2):
    '''
    Criterio L-L-A (lado - lado - ángulo).
    Se reciben dos triángulos, cada uno como una tupla con dos lados y un
    ángulo que NO está entre ellos, sino opuesto al primer lado.
    t1: (a, b, alfa) primer triángulo
    t2: (a, b, alfa) segundo triángulo
    a: lado opuesto al ángulo alfa
    b: otro lado
    alfa: ángulo (en grados) opuesto al lado a

    Regla: dos triángulos con dos lados y un ángulo no comprendido iguales
    solo son congruentes si el ángulo es opuesto al lado mayor (a >= b).
    Si a < b es el "caso ambiguo": con esos datos pueden existir dos
    triángulos distintos, así que el criterio no garantiza la congruencia.

    Se lanza ValueError si algún lado es menor o igual a 0, si el ángulo no
    está entre 0 y 180 grados, si con a == b el ángulo es de 90 o más
    (no se forma triángulo), o si a < b (caso ambiguo).

    Se retorna True si los triángulos son congruentes, False si no.
    '''
    for a, b, alfa in (t1, t2):
        validar_lados(a, b)
        validar_angulo(alfa)
        if a < b:
            raise ValueError(
                f"Caso ambiguo: el ángulo {alfa} es opuesto al lado menor ({a} < {b}); "
                "L-L-A no garantiza la congruencia."
            )
        if iguales(a, b) and alfa >= 90:
            raise ValueError("Con a == b el ángulo debe ser menor que 90 grados.")

    return all(iguales(x, y) for x, y in zip(t1, t2))