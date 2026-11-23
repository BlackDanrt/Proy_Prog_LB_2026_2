import math
import matplotlib.pyplot as plt
from poligonos.area import area_poligono, area_poligono_regular
from poligonos.perimetro import calcularPerimetro, perimetro_poligono_regular
from poligonos.clasificacion.clasificacion_poligonos import clasificar_por_forma, clasificar_por_lados
from poligonos.diagonales.diagonales import numero_total_diagonales, diagonales_desde_un_vertice
from poligonos.especiales.poligonos_especiales import es_equilatero, es_equiangulo
from validaciones import validar_poligono, validar_numero_lados, validar_lados


def _dibujar_poligono(ax, vertices, color="tab:blue"):
    '''
    Se recibe un eje de matplotlib y la lista de vértices de un polígono.
    ax: eje donde se dibuja
    vertices: lista de tuplas (x, y)
    color: color del polígono

    Se dibuja el polígono relleno con sus vértices numerados (V1, V2, ...).
    '''
    xs = [v[0] for v in vertices] + [vertices[0][0]]
    ys = [v[1] for v in vertices] + [vertices[0][1]]
    ax.fill(xs, ys, alpha=0.25, color=color)
    ax.plot(xs, ys, "o-", color=color)

    n = len(vertices)
    cx = sum(v[0] for v in vertices) / n
    cy = sum(v[1] for v in vertices) / n
    for i, (x, y) in enumerate(vertices, start=1):
        ax.annotate(f"V{i}", (x, y), xytext=(x + (x - cx) * 0.12, y + (y - cy) * 0.12),
                    ha="center", va="center", fontweight="bold")

    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.margins(0.15)


def graficar_poligono(vertices):
    '''
    Se recibe la lista de vértices de un polígono, en orden.
    vertices: lista de tuplas (x, y)

    Se dibuja el polígono. En el título se muestra su nombre según el número
    de lados, si es convexo o cóncavo, su área y su perímetro.

    Se lanza ValueError si los vértices no forman un polígono simple válido
    (ver validar_poligono).
    '''
    nombre = clasificar_por_lados(len(vertices))
    forma = clasificar_por_forma(vertices)
    area = area_poligono(vertices)
    perimetro = calcularPerimetro(vertices)

    fig, ax = plt.subplots()
    _dibujar_poligono(ax, vertices, color="tab:red" if forma == "cóncavo" else "tab:blue")
    ax.set_title(f"{nombre.capitalize()} {forma}\nÁrea = {area}   Perímetro = {perimetro}")
    plt.show()


def graficar_diagonales(vertices, vertice=1):
    '''
    Se recibe la lista de vértices de un polígono y el vértice a resaltar.
    vertices: lista de tuplas (x, y)
    vertice: número del vértice (de 1 a n) cuyas diagonales se resaltan

    Se dibujan todas las diagonales en gris y las que salen del vértice
    elegido en rojo. En el título se muestra el número total de diagonales
    y el número de diagonales desde un vértice.

    Se lanza ValueError si los vértices no forman un polígono simple válido,
    o si el vértice no está entre 1 y n.
    '''
    validar_poligono(vertices)
    n = len(vertices)
    if isinstance(vertice, bool) or not isinstance(vertice, int) or not 1 <= vertice <= n:
        raise ValueError(f"El vértice debe ser un entero entre 1 y {n} (se recibió {vertice!r}).")

    total = numero_total_diagonales(n)
    desde_uno = diagonales_desde_un_vertice(n)
    elegido = vertice - 1

    fig, ax = plt.subplots()
    for i in range(n):
        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue  # V1 y Vn son vecinos, no forman diagonal
            resaltada = elegido in (i, j)
            ax.plot([vertices[i][0], vertices[j][0]], [vertices[i][1], vertices[j][1]],
                    color="red" if resaltada else "gray",
                    lw=2 if resaltada else 1,
                    ls="-" if resaltada else "--",
                    zorder=3 if resaltada else 2)

    _dibujar_poligono(ax, vertices)
    ax.set_title(f"{clasificar_por_lados(n).capitalize()}: {total} diagonales en total\n"
                 f"Desde V{vertice} salen {desde_uno} (en rojo)")
    plt.show()


def vertices_poligono_regular(n, l):
    '''
    Se recibe el número de lados y la longitud del lado de un polígono regular.
    n: número de lados (entero mayor o igual a 3)
    l: longitud del lado

    Formula: se ubican los vértices sobre una circunferencia de radio
        R = l / (2 * sen(π / n))
    separados por ángulos de 360° / n, con el primer lado horizontal abajo.

    Se lanza ValueError si n no es un entero mayor o igual a 3, o si el lado
    es menor o igual a 0.

    Se retorna la lista de vértices (x, y) del polígono regular.
    '''
    validar_numero_lados(n)
    validar_lados(l)
    radio = l / (2 * math.sin(math.pi / n))
    inicio = -math.pi / 2 - math.pi / n  # deja el primer lado horizontal en la parte de abajo
    return [(radio * math.cos(inicio + 2 * math.pi * k / n),
             radio * math.sin(inicio + 2 * math.pi * k / n)) for k in range(n)]


def graficar_poligono_regular(n, l):
    '''
    Se recibe el número de lados y la longitud del lado de un polígono regular.
    n: número de lados (entero mayor o igual a 3)
    l: longitud del lado

    Se dibuja el polígono regular con su apotema. En el título se muestra
    su nombre, si es equilátero y equiángulo, su área y su perímetro.

    Se lanza ValueError si n no es un entero mayor o igual a 3, o si el lado
    es menor o igual a 0.
    '''
    vertices = vertices_poligono_regular(n, l)
    area = area_poligono_regular(n, l)
    perimetro = perimetro_poligono_regular(n, l)
    equilatero = "Sí" if es_equilatero(vertices) else "No"
    equiangulo = "Sí" if es_equiangulo(vertices) else "No"

    fig, ax = plt.subplots()
    _dibujar_poligono(ax, vertices, color="tab:green")

    # Apotema: del centro al punto medio del primer lado
    medio = ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2)
    apotema = math.hypot(*medio)
    ax.plot(0, 0, "ko")
    ax.plot([0, medio[0]], [0, medio[1]], color="darkred", lw=2)
    ax.text(0, medio[1] / 2, f" apotema = {apotema:.3f}", color="darkred", va="center")

    ax.set_title(f"{clasificar_por_lados(n).capitalize()} regular de lado {l}\n"
                 f"Equilátero: {equilatero}   Equiángulo: {equiangulo}   "
                 f"Área = {area}   Perímetro = {perimetro}")
    plt.show()