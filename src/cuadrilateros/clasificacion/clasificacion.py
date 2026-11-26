from validaciones import iguales

def _producto_cruz(ux, uy, vx, vy):
    '''
    Se reciben dos vectores u = (ux, uy) y v = (vx, vy).

    Formula: u x v = ux * vy - uy * vx

    Se retorna 0 si los vectores son paralelos; su signo indica el sentido del giro.
    '''
    return ux * vy - uy * vx


def _producto_punto(ux, uy, vx, vy):
    '''
    Se reciben dos vectores u = (ux, uy) y v = (vx, vy).

    Formula: u · v = ux * vx + uy * vy

    Se retorna 0 si los vectores son perpendiculares.
    '''
    return ux * vx + uy * vy


def _longitud(ux, uy):
    '''
    Se recibe un vector u = (ux, uy).

    Formula: |u| = sqrt(ux² + uy²)

    Se retorna la longitud del vector.
    '''
    return (ux ** 2 + uy ** 2) ** 0.5


def _segmentos_se_cruzan(p1, p2, p3, p4):
    '''
    Se reciben los extremos de dos segmentos: p1-p2 y p3-p4.

    Se retorna True si los segmentos se cruzan en un punto interior.
    '''
    def orientacion(a, b, c):
        return _producto_cruz(b[0] - a[0], b[1] - a[1], c[0] - a[0], c[1] - a[1])

    d1 = orientacion(p3, p4, p1)
    d2 = orientacion(p3, p4, p2)
    d3 = orientacion(p1, p2, p3)
    d4 = orientacion(p1, p2, p4)
    return d1 * d2 < 0 and d3 * d4 < 0


def clasificar_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4):
    '''
    Se recibe como parametro 8 variables que corresponden a los 4 puntos (x,y)
    que conforman un cuadrilatero, dados en orden (horario o antihorario).

    Regla:
        cóncavo     -> tiene un ángulo interior mayor de 180°
        convexo:
            trapezoide    -> ningún par de lados opuestos es paralelo
            trapecio      -> exactamente un par de lados opuestos es paralelo
                rectángulo  -> un lado no paralelo es perpendicular a las bases
                isósceles   -> los dos lados no paralelos miden igual
                escaleno    -> los dos lados no paralelos miden distinto
            paralelogramo -> los dos pares de lados opuestos son paralelos
                cuadrado    -> lados iguales y ángulos rectos
                rectángulo  -> ángulos rectos y lados contiguos distintos
                rombo       -> lados iguales y ángulos no rectos
                romboide    -> lados contiguos distintos y ángulos no rectos

    Se lanza ValueError si tres puntos consecutivos están sobre una misma
    recta (incluye puntos repetidos), o si dos lados opuestos se cruzan.

    Se retorna un texto con la clasificación más específica:
    "cóncavo", "trapezoide", "trapecio rectángulo", "trapecio isósceles",
    "trapecio escaleno", "romboide", "rombo", "rectángulo" o "cuadrado".
    '''
    puntos = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

    lados = []
    for i in range(4):
        (ax, ay), (bx, by) = puntos[i], puntos[(i + 1) % 4]
        lados.append((bx - ax, by - ay))

    giros = []
    for i in range(4):
        giro = _producto_cruz(*lados[i], *lados[(i + 1) % 4])
        if iguales(giro, 0):
            raise ValueError(
                f"Los puntos {puntos[i]}, {puntos[(i + 1) % 4]} y {puntos[(i + 2) % 4]} "
                "son colineales o están repetidos; no forman un cuadrilátero."
            )
        giros.append(giro)

    if _segmentos_se_cruzan(puntos[0], puntos[1], puntos[2], puntos[3]) or \
       _segmentos_se_cruzan(puntos[1], puntos[2], puntos[3], puntos[0]):
        raise ValueError(
            "Dos lados opuestos se cruzan; los puntos deben darse en orden "
            "(horario o antihorario) alrededor del cuadrilátero."
        )

    if not (all(g > 0 for g in giros) or all(g < 0 for g in giros)):
        return "cóncavo"

    paralelos_02 = iguales(_producto_cruz(*lados[0], *lados[2]), 0)
    paralelos_13 = iguales(_producto_cruz(*lados[1], *lados[3]), 0)

    if not paralelos_02 and not paralelos_13:
        return "trapezoide"

    if paralelos_02 and paralelos_13:
        lados_iguales = iguales(_longitud(*lados[0]), _longitud(*lados[1]))
        angulo_recto = iguales(_producto_punto(*lados[0], *lados[1]), 0)
        if lados_iguales and angulo_recto:
            return "cuadrado"
        if angulo_recto:
            return "rectángulo"
        if lados_iguales:
            return "rombo"
        return "romboide"

    if paralelos_02:
        base, no_paralelo_1, no_paralelo_2 = lados[0], lados[1], lados[3]
    else:
        base, no_paralelo_1, no_paralelo_2 = lados[1], lados[0], lados[2]

    if iguales(_producto_punto(*base, *no_paralelo_1), 0) or \
       iguales(_producto_punto(*base, *no_paralelo_2), 0):
        return "trapecio rectángulo"
    if iguales(_longitud(*no_paralelo_1), _longitud(*no_paralelo_2)):
        return "trapecio isósceles"
    return "trapecio escaleno"