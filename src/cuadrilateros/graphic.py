import math
import matplotlib.pyplot as plt
from cuadrilateros.perimetro import calcularPerimetro
from cuadrilateros.clasificacion.clasificacion import clasificar_cuadrilatero


def _area_coordenadas(puntos):
    '''
    Se recibe la lista de vértices de un cuadrilátero, en orden.
    puntos: lista de cuatro tuplas (x, y)

    Formula (fórmula del área de Gauss):
        Área = |Σ (x_i * y_(i+1) - x_(i+1) * y_i)| / 2

    Se usa porque las funciones de areas.py reciben base y altura, no coordenadas.

    Se retorna el área del cuadrilátero con 3 decimales.
    '''
    suma = 0
    for i in range(4):
        x1, y1 = puntos[i]
        x2, y2 = puntos[(i + 1) % 4]
        suma += x1 * y2 - x2 * y1
    return round(abs(suma) / 2, 3)


def graficar_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4):
    '''
    Se reciben las coordenadas de los cuatro vértices de un cuadrilátero, en orden.
    x1, y1: vértice A
    x2, y2: vértice B
    x3, y3: vértice C
    x4, y4: vértice D

    Se dibuja el cuadrilátero con la longitud de sus lados y sus dos
    diagonales en línea punteada. En el título se muestra su clasificación,
    su perímetro y su área.

    Se lanza ValueError si hay puntos repetidos o colineales, o si los lados
    se cruzan (ver calcularPerimetro y clasificar_cuadrilatero).
    '''
    perimetro = calcularPerimetro(x1, y1, x2, y2, x3, y3, x4, y4)
    tipo = clasificar_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4)
    puntos = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    area = _area_coordenadas(puntos)

    fig, ax = plt.subplots()
    xs = [p[0] for p in puntos] + [x1]
    ys = [p[1] for p in puntos] + [y1]
    ax.fill(xs, ys, alpha=0.25, color="tab:purple")
    ax.plot(xs, ys, "o-", color="tab:purple")

    # Diagonales AC y BD
    ax.plot([x1, x3], [y1, y3], "--", color="gray")
    ax.plot([x2, x4], [y2, y4], "--", color="gray")

    cx = sum(p[0] for p in puntos) / 4
    cy = sum(p[1] for p in puntos) / 4
    for nombre, (x, y) in zip("ABCD", puntos):
        ax.annotate(nombre, (x, y), xytext=(x + (x - cx) * 0.12, y + (y - cy) * 0.12),
                    ha="center", va="center", fontweight="bold")

    for i in range(4):
        p, q = puntos[i], puntos[(i + 1) % 4]
        longitud = math.sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)
        ax.text((p[0] + q[0]) / 2, (p[1] + q[1]) / 2, f"{longitud:.2f}",
                ha="center", va="center", fontsize=9,
                bbox=dict(boxstyle="round", fc="white", ec="tab:purple", alpha=0.8))

    ax.set_title(f"Cuadrilátero: {tipo}\nPerímetro = {perimetro}   Área = {area}")
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.margins(0.15)
    plt.show()