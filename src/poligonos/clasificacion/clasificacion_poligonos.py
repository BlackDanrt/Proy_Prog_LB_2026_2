from validaciones import validar_poligono, validar_numero_lados, producto_cruz


NOMBRES_POLIGONOS = {
    3: "triángulo",
    4: "cuadrilátero",
    5: "pentágono",
    6: "hexágono",
    7: "heptágono",
    8: "octágono",
    9: "eneágono",
    10: "decágono",
    11: "endecágono",
    12: "dodecágono",
    13: "tridecágono",
    14: "tetradecágono",
    15: "pentadecágono",
    16: "hexadecágono",
    17: "heptadecágono",
    18: "octadecágono",
    19: "eneadecágono",
    20: "icoságono",
}


def clasificar_por_forma(vertices):
    '''
    Se recibe la lista de vértices de un polígono, en orden.
    vertices: lista de tuplas (x, y)

    Criterio: se calcula el producto cruz en cada vértice
    (anterior -> actual -> siguiente).
        - Si todos tienen el mismo signo, todos los giros van hacia el mismo
          lado y el polígono es convexo (todos sus ángulos interiores < 180°).
        - Si hay signos distintos, al menos un ángulo interior es > 180°
          y el polígono es cóncavo.

    Se lanza ValueError si los vértices no forman un polígono simple válido
    (ver validar_poligono).

    Se retorna "convexo" o "cóncavo".
    '''
    validar_poligono(vertices)
    n = len(vertices)

    positivos = 0
    negativos = 0
    for i in range(n):
        cruz = producto_cruz(vertices[i - 1], vertices[i], vertices[(i + 1) % n])
        if cruz > 0:
            positivos += 1
        else:
            negativos += 1

    if positivos == 0 or negativos == 0:
        return "convexo"
    return "cóncavo"


def clasificar_por_lados(n):
    '''
    Se recibe el número de lados de un polígono.
    n: número de lados (entero mayor o igual a 3)

    Se lanza ValueError si n no es un entero o es menor que 3.

    Se retorna el nombre del polígono ("triángulo", "pentágono", ...).
    Si n es mayor que 20 se retorna "polígono de n lados".
    '''
    validar_numero_lados(n)
    return NOMBRES_POLIGONOS.get(n, f"polígono de {n} lados")
