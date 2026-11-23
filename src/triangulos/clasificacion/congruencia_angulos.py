from validaciones import validar_angulo, iguales


def clasificar_por_angulos(alfa, beta, gamma):
    '''
    Se reciben los tres ángulos internos de un triángulo.
    alfa, beta, gamma: ángulos en grados

    Regla: rectángulo     -> tiene un ángulo de 90°
           oblicuángulo   -> no tiene ningún ángulo de 90°, y puede ser:
               acutángulo  -> los tres ángulos son menores de 90°
               obtusángulo -> tiene un ángulo mayor de 90°

    Se lanza ValueError si algún ángulo no está estrictamente entre 0 y 180
    grados, o si la suma de los tres ángulos no es 180 grados.

    Se retorna "rectángulo", "acutángulo" u "obtusángulo"
    (los dos últimos son los tipos de oblicuángulo).
    '''
    for angulo in (alfa, beta, gamma):
        validar_angulo(angulo)
    if not iguales(alfa + beta + gamma, 180):
        raise ValueError(
            f"La suma de los ángulos debe ser 180° (se recibió {alfa + beta + gamma}°)."
        )

    mayor = max(alfa, beta, gamma)
    if iguales(mayor, 90):
        return "rectángulo"
    if mayor > 90:
        return "obtusángulo"
    return "acutángulo"