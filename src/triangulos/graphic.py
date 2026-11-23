import math
import matplotlib.pyplot as plt
from triangulos.perimetro import calcularPerimetro
from triangulos.area import area_triangulo_escaleno
from triangulos.clasificacion.congruencia import clasificar_por_lados
from triangulos.clasificacion.congruencia_angulos import clasificar_por_angulos
from triangulos.calculo.notables import triangulo_notable
from triangulos.calculo.angulos_aproximados import triangulo_aproximado
from triangulos.congruentes.lll import congruencia_lll
from triangulos.congruentes.lal import congruencia_lal
from triangulos.congruentes.ala import congruencia_ala
from triangulos.congruentes.lla import congruencia_lla


def _distancia(p, q):
    '''
    Se reciben dos puntos (x, y).

    Formula: d = sqrt((x2 - x1)² + (y2 - y1)²)

    Se retorna la distancia entre los dos puntos.
    '''
    return math.sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)


def _angulo_en(vertice, p, q):
    '''
    Se reciben tres puntos: el vértice del ángulo y los otros dos vértices.

    Formula: ángulo = acos((u · v) / (|u| * |v|)), con u = p - vértice y v = q - vértice

    Se retorna el ángulo en el vértice, en grados.
    '''
    ux, uy = p[0] - vertice[0], p[1] - vertice[1]
    vx, vy = q[0] - vertice[0], q[1] - vertice[1]
    coseno = (ux * vx + uy * vy) / (math.hypot(ux, uy) * math.hypot(vx, vy))
    coseno = max(-1.0, min(1.0, coseno))  # evita errores de redondeo fuera de [-1, 1]
    return math.degrees(math.acos(coseno))


def _dibujar_triangulo(ax, puntos, nombres=("A", "B", "C"), color="tab:blue"):
    '''
    Se recibe un eje de matplotlib y los tres vértices de un triángulo.
    ax: eje donde se dibuja
    puntos: lista de tres tuplas (x, y)
    nombres: nombres de los vértices
    color: color del triángulo

    Se dibuja el triángulo relleno, el nombre de cada vértice y la longitud
    de cada lado en su punto medio.
    '''
    xs = [p[0] for p in puntos] + [puntos[0][0]]
    ys = [p[1] for p in puntos] + [puntos[0][1]]
    ax.fill(xs, ys, alpha=0.25, color=color)
    ax.plot(xs, ys, "o-", color=color)

    cx = sum(p[0] for p in puntos) / 3
    cy = sum(p[1] for p in puntos) / 3
    for nombre, (x, y) in zip(nombres, puntos):
        # El nombre se corre un poco hacia afuera del triángulo
        ax.annotate(nombre, (x, y), xytext=(x + (x - cx) * 0.12, y + (y - cy) * 0.12),
                    ha="center", va="center", fontweight="bold")

    for i in range(3):
        p, q = puntos[i], puntos[(i + 1) % 3]
        ax.text((p[0] + q[0]) / 2, (p[1] + q[1]) / 2, f"{_distancia(p, q):.2f}",
                ha="center", va="center", fontsize=9,
                bbox=dict(boxstyle="round", fc="white", ec=color, alpha=0.8))

    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)


def graficar_triangulo(x1, y1, x2, y2, x3, y3):
    '''
    Se reciben las coordenadas de los tres vértices de un triángulo.
    x1, y1: vértice A
    x2, y2: vértice B
    x3, y3: vértice C

    Se dibuja el triángulo con la longitud de sus lados y sus ángulos internos.
    En el título se muestra su clasificación por lados y por ángulos, su
    perímetro y su área (fórmula de Herón).

    Se lanza ValueError si los puntos son colineales (no forman triángulo).
    '''
    perimetro = calcularPerimetro(x1, y1, x2, y2, x3, y3)

    A, B, C = (x1, y1), (x2, y2), (x3, y3)
    a, b, c = _distancia(B, C), _distancia(A, C), _distancia(A, B)
    alfa, beta = _angulo_en(A, B, C), _angulo_en(B, A, C)
    gamma = 180 - alfa - beta

    por_lados = clasificar_por_lados(a, b, c)
    por_angulos = clasificar_por_angulos(alfa, beta, gamma)
    area = area_triangulo_escaleno(a, b, c)

    fig, ax = plt.subplots()
    _dibujar_triangulo(ax, [A, B, C])

    cx, cy = (x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3
    for (x, y), angulo in zip((A, B, C), (alfa, beta, gamma)):
        # El ángulo se escribe un poco hacia adentro del triángulo
        ax.text(x + (cx - x) * 0.25, y + (cy - y) * 0.25, f"{angulo:.1f}°",
                ha="center", va="center", fontsize=9, color="darkred")

    ax.set_title(f"Triángulo {por_lados} y {por_angulos}\n"
                 f"Perímetro = {perimetro}   Área = {area}")
    plt.show()


def _graficar_rectangulo(angulo, opuesto, adyacente, hipotenusa, titulo):
    '''
    Se recibe un ángulo agudo y los tres lados de un triángulo rectángulo.

    Se dibuja el triángulo con el cateto adyacente sobre el eje x, el cateto
    opuesto en vertical, el ángulo recto marcado y cada lado rotulado.
    '''
    A, B, C = (0, 0), (adyacente, 0), (adyacente, opuesto)

    fig, ax = plt.subplots()
    xs, ys = [A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]]
    ax.fill(xs, ys, alpha=0.25, color="tab:green")
    ax.plot(xs, ys, "o-", color="tab:green")

    # Cuadrito del ángulo recto
    t = min(opuesto, adyacente) * 0.08
    ax.plot([adyacente - t, adyacente - t, adyacente], [0, t, t], color="black", lw=1)

    # Arco del ángulo dado
    radio = min(opuesto, adyacente) * 0.25
    arco = [math.radians(angulo) * k / 30 for k in range(31)]
    ax.plot([radio * math.cos(r) for r in arco], [radio * math.sin(r) for r in arco],
            color="darkred")
    ax.text(radio * 1.2, radio * 0.35, f"{angulo}°", color="darkred")

    caja = dict(boxstyle="round", fc="white", ec="tab:green", alpha=0.8)
    ax.text(adyacente / 2, 0, f"adyacente = {adyacente:.3f}", ha="center", va="top", bbox=caja)
    ax.text(adyacente, opuesto / 2, f" opuesto = {opuesto:.3f}", ha="left", va="center", bbox=caja)
    ax.text(adyacente / 2, opuesto / 2, f"hipotenusa = {hipotenusa:.3f}",
            ha="right", va="bottom", bbox=caja)

    ax.set_title(titulo)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.margins(0.25)
    plt.show()


def graficar_notable(angulo, lado, tipo):
    '''
    Se recibe un ángulo notable y uno de los lados de un triángulo rectángulo.
    angulo: ángulo agudo en grados (15, 30, 45, 60 o 75)
    lado: longitud del lado conocido
    tipo: "opuesto", "adyacente" o "hipotenusa"

    Se calculan los tres lados con triangulo_notable y se dibuja el triángulo.

    Se lanza ValueError si el ángulo no es notable, si el lado es menor o
    igual a 0, o si el tipo de lado no es válido.
    '''
    opuesto, adyacente, hipotenusa = triangulo_notable(angulo, lado, tipo)
    _graficar_rectangulo(angulo, opuesto, adyacente, hipotenusa,
                         f"Triángulo notable de {angulo}° ({tipo} = {lado})")


def graficar_aproximado(angulo, lado, tipo):
    '''
    Se recibe un ángulo aproximado y uno de los lados de un triángulo rectángulo.
    angulo: ángulo agudo en grados (8, 16, 37, 53, 74 u 82)
    lado: longitud del lado conocido
    tipo: "opuesto", "adyacente" o "hipotenusa"

    Se calculan los tres lados con triangulo_aproximado y se dibuja el triángulo.

    Se lanza ValueError si el ángulo no es válido, si el lado es menor o
    igual a 0, o si el tipo de lado no es válido.
    '''
    opuesto, adyacente, hipotenusa = triangulo_aproximado(angulo, lado, tipo)
    _graficar_rectangulo(angulo, opuesto, adyacente, hipotenusa,
                         f"Triángulo aproximado de {angulo}° ({tipo} = {lado})")


def _vertices_desde_criterio(t, criterio):
    '''
    Se recibe un triángulo dado según un criterio de congruencia.
    t: tupla con los datos del triángulo, en el mismo formato de cada criterio
       LLL: (a, b, c)   LAL: (a, gamma, b)   ALA: (alfa, c, beta)   LLA: (a, b, alfa)
    criterio: "LLL", "LAL", "ALA" o "LLA"

    Se construyen las coordenadas del triángulo poniendo un lado sobre el eje x.

    Se retorna una lista con los tres vértices (x, y).
    '''
    if criterio == "LLL":
        a, b, c = t
        x = (b * b + c * c - a * a) / (2 * c)
        return [(0, 0), (c, 0), (x, math.sqrt(max(b * b - x * x, 0)))]

    if criterio == "LAL":
        a, gamma, b = t
        g = math.radians(gamma)
        return [(0, 0), (a, 0), (b * math.cos(g), b * math.sin(g))]

    if criterio == "ALA":
        alfa, c, beta = t
        gamma = math.radians(180 - alfa - beta)
        lado_ac = c * math.sin(math.radians(beta)) / math.sin(gamma)  # ley de senos
        al = math.radians(alfa)
        return [(0, 0), (c, 0), (lado_ac * math.cos(al), lado_ac * math.sin(al))]

    # LLA: el ángulo alfa está en el origen, b sobre el eje x y a es opuesto a alfa
    a, b, alfa = t
    al = math.radians(alfa)
    c = b * math.cos(al) + math.sqrt(max(a * a - (b * math.sin(al)) ** 2, 0))
    return [(0, 0), (b, 0), (c * math.cos(al), c * math.sin(al))]


def graficar_congruencia(t1, t2, criterio):
    '''
    Se reciben dos triángulos y el criterio de congruencia con el que se comparan.
    t1: datos del primer triángulo
    t2: datos del segundo triángulo
        LLL: (a, b, c)   LAL: (a, gamma, b)   ALA: (alfa, c, beta)   LLA: (a, b, alfa)
    criterio: "LLL", "LAL", "ALA" o "LLA"

    Se dibujan los dos triángulos lado a lado y en el título se indica si
    son congruentes según el criterio.

    Se lanza ValueError si el criterio no es válido, o si los datos no
    cumplen las validaciones del criterio (ver congruencia_lll, congruencia_lal,
    congruencia_ala y congruencia_lla).
    '''
    funciones = {
        "LLL": congruencia_lll,
        "LAL": congruencia_lal,
        "ALA": congruencia_ala,
        "LLA": congruencia_lla,
    }
    if criterio not in funciones:
        raise ValueError(f"Criterio '{criterio}' no válido. Use uno de: {list(funciones)}.")

    son_congruentes = funciones[criterio](t1, t2)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    _dibujar_triangulo(ax1, _vertices_desde_criterio(t1, criterio), color="tab:blue")
    _dibujar_triangulo(ax2, _vertices_desde_criterio(t2, criterio),
                       nombres=("A'", "B'", "C'"), color="tab:orange")
    ax1.set_title(f"Triángulo 1: {t1}")
    ax2.set_title(f"Triángulo 2: {t2}")

    resultado = "Congruentes" if son_congruentes else "No congruentes"
    fig.suptitle(f"Criterio {criterio}: {resultado}", fontsize=14, fontweight="bold",
                 color="green" if son_congruentes else "red")
    plt.show()