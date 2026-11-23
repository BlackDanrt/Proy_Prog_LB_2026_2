from validaciones import validar_numero_lados


def numero_total_diagonales(n):
    '''
    Se recibe el número de lados de un polígono.
    n: número de lados (entero mayor o igual a 3)

    Formula: D = n * (n - 3) / 2

    Se lanza ValueError si n no es un entero o es menor que 3.

    Se retorna el número total de diagonales del polígono.
    '''
    validar_numero_lados(n)
    return n * (n - 3) // 2


def diagonales_desde_un_vertice(n):
    '''
    Se recibe el número de lados de un polígono.
    n: número de lados (entero mayor o igual a 3)

    Formula: d = n - 3
    (desde un vértice no se traza diagonal hacia sí mismo ni hacia sus
    dos vértices vecinos)

    Se lanza ValueError si n no es un entero o es menor que 3.

    Se retorna el número de diagonales trazadas desde un vértice.
    '''
    validar_numero_lados(n)
    return n - 3


def diagonales_desde_m_vertices(n, m):
    '''
    Se recibe el número de lados de un polígono y una cantidad de vértices consecutivos.
    n: número de lados (entero mayor o igual a 3)
    m: número de vértices consecutivos desde los que se trazan diagonales
       (entero entre 1 y n)

    Formula: D_m = m * n - (m + 1) * (m + 2) / 2

    La fórmula es válida para 1 <= m <= n - 1. Si m = n se están tomando
    todos los vértices, así que se retorna el número total de diagonales.

    Se lanza ValueError si n no es un entero mayor o igual a 3, o si m no es
    un entero entre 1 y n.

    Se retorna el número de diagonales trazadas desde los m vértices consecutivos.
    '''
    validar_numero_lados(n)
    if isinstance(m, bool) or not isinstance(m, int):
        raise ValueError(f"El número de vértices debe ser un entero, se recibió {m!r}.")
    if m < 1 or m > n:
        raise ValueError(f"El número de vértices consecutivos debe estar entre 1 y {n}, se recibió {m}.")
    if m == n:
        return numero_total_diagonales(n)
    return m * n - (m + 1) * (m + 2) // 2
