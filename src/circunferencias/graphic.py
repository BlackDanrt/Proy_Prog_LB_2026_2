import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from circunferencias.area import calcularArea
from circunferencias.tangentes.comun_dos_circunferencias import (
    tangente_comun_exterior,
    tangente_comun_interior,
)


def graficar_circunferencia(radio):
    '''
    Se recibe el radio de una circunferencia.
    radio: radio de la circunferencia

    Se dibuja el círculo sombreado con su centro y su radio. En el título
    se muestra el área.

    Se lanza ValueError si el radio es menor o igual a 0.
    '''
    area = calcularArea(radio)

    fig, ax = plt.subplots()
    ax.add_patch(Circle((0, 0), radio, alpha=0.25, color="tab:blue"))
    ax.add_patch(Circle((0, 0), radio, fill=False, color="tab:blue", lw=2))
    ax.plot(0, 0, "ko")
    ax.plot([0, radio], [0, 0], color="darkred", lw=2)
    ax.text(radio / 2, 0, f"r = {radio}", ha="center", va="bottom", color="darkred")

    ax.set_title(f"Circunferencia de radio {radio}\nÁrea = {area}")
    ax.set_xlim(-radio * 1.3, radio * 1.3)
    ax.set_ylim(-radio * 1.3, radio * 1.3)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    plt.show()


def _dibujar_dos_circunferencias(ax, r1, r2, d):
    '''
    Se recibe un eje de matplotlib, los dos radios y la distancia entre centros.

    Se dibujan las dos circunferencias con centros en (0, 0) y (d, 0), y el
    segmento que une los centros.
    '''
    for centro, r, color in (((0, 0), r1, "tab:blue"), ((d, 0), r2, "tab:orange")):
        ax.add_patch(Circle(centro, r, alpha=0.15, color=color))
        ax.add_patch(Circle(centro, r, fill=False, color=color, lw=2))
        ax.plot(*centro, "ko")
    ax.plot([0, d], [0, 0], ":", color="gray")
    ax.text(d / 2, 0, f"d = {d}", ha="center", va="top", color="gray")


def _ajustar_ejes(ax, r1, r2, d):
    '''
    Se ajustan los límites del eje para que se vean completas las dos circunferencias.
    '''
    margen = max(r1, r2) * 0.3
    ax.set_xlim(-r1 - margen, d + r2 + margen)
    ax.set_ylim(-max(r1, r2) - margen, max(r1, r2) + margen)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)


def graficar_tangente_exterior(r1, r2, d):
    '''
    Se reciben los radios de dos circunferencias y la distancia entre sus centros.
    r1: radio de la primera circunferencia
    r2: radio de la segunda circunferencia
    d: distancia entre los centros

    Se dibujan las dos circunferencias y sus dos tangentes comunes exteriores.
    Los puntos de tangencia se ubican con el ángulo θ, donde cos θ = (r1 - r2) / d:
        P1 = C1 + r1 * (cos θ, sen θ)
        P2 = C2 + r2 * (cos θ, sen θ)

    Se lanza ValueError en los mismos casos que tangente_comun_exterior.
    '''
    longitud = tangente_comun_exterior(r1, r2, d)

    fig, ax = plt.subplots()
    _dibujar_dos_circunferencias(ax, r1, r2, d)

    theta = math.acos((r1 - r2) / d)
    for signo in (1, -1):
        ux, uy = math.cos(theta), signo * math.sin(theta)
        p1 = (r1 * ux, r1 * uy)
        p2 = (d + r2 * ux, r2 * uy)
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="darkred", lw=2)
        ax.plot(*zip(p1, p2), "o", color="darkred")
        ax.plot([0, p1[0]], [0, p1[1]], "--", color="tab:blue", lw=1)
        ax.plot([d, p2[0]], [0, p2[1]], "--", color="tab:orange", lw=1)

    ax.set_title(f"Tangente común exterior (r1 = {r1}, r2 = {r2}, d = {d})\n"
                 f"Longitud = {longitud:.3f}")
    _ajustar_ejes(ax, r1, r2, d)
    plt.show()


def graficar_tangente_interior(r1, r2, d):
    '''
    Se reciben los radios de dos circunferencias y la distancia entre sus centros.
    r1: radio de la primera circunferencia
    r2: radio de la segunda circunferencia
    d: distancia entre los centros

    Se dibujan las dos circunferencias y sus dos tangentes comunes interiores
    (las que se cruzan entre los dos círculos).
    Los puntos de tangencia se ubican con el ángulo θ, donde cos θ = (r1 + r2) / d:
        P1 = C1 + r1 * (cos θ, sen θ)
        P2 = C2 - r2 * (cos θ, sen θ)

    Se lanza ValueError en los mismos casos que tangente_comun_interior.
    '''
    longitud = tangente_comun_interior(r1, r2, d)

    fig, ax = plt.subplots()
    _dibujar_dos_circunferencias(ax, r1, r2, d)

    theta = math.acos((r1 + r2) / d)
    for signo in (1, -1):
        ux, uy = math.cos(theta), signo * math.sin(theta)
        p1 = (r1 * ux, r1 * uy)
        p2 = (d - r2 * ux, -r2 * uy)
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="darkred", lw=2)
        ax.plot(*zip(p1, p2), "o", color="darkred")
        ax.plot([0, p1[0]], [0, p1[1]], "--", color="tab:blue", lw=1)
        ax.plot([d, p2[0]], [0, p2[1]], "--", color="tab:orange", lw=1)

    ax.set_title(f"Tangente común interior (r1 = {r1}, r2 = {r2}, d = {d})\n"
                 f"Longitud = {longitud:.3f}")
    _ajustar_ejes(ax, r1, r2, d)
    plt.show()