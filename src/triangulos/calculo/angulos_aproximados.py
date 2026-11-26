import math
from validaciones import validar_lados

# Proporciones (cateto opuesto, cateto adyacente, hipotenusa) para cada ángulo agudo.
# Son relaciones APROXIMADAS
PROPORCIONES_APROXIMADAS = {
    8:  (1, 7, 5 * math.sqrt(2)),
    16: (7, 24, 25),
    37: (3, 4, 5),
    53: (4, 3, 5),
    74: (24, 7, 25),
    82: (7, 1, 5 * math.sqrt(2)),
}

TIPOS_LADO = ("opuesto", "adyacente", "hipotenusa")


def triangulo_aproximado(angulo, lado, tipo):
    '''
    Se recibe un ángulo agudo aproximado de un triángulo rectángulo y la
    longitud de uno de sus lados.
    angulo: ángulo agudo en grados (8, 16, 37, 53, 74 u 82)
    lado: longitud del lado conocido
    tipo: qué lado es, respecto al ángulo: "opuesto", "adyacente" o "hipotenusa"

    Formula: cada ángulo aproximado tiene lados en una proporción fija
             (opuesto : adyacente : hipotenusa), por ejemplo
             37° -> 3 : 4 : 5      53° -> 4 : 3 : 5
             16° -> 7 : 24 : 25    74° -> 24 : 7 : 25
             8°  -> 1 : 7 : 5√2    82° -> 7 : 1 : 5√2
             Si el lado conocido equivale a p partes, cada parte mide k = lado / p,
             y los demás lados se obtienen multiplicando su proporción por k.
             Los resultados son aproximados

    Se lanza ValueError si el ángulo no es uno de los aproximados, si el lado
    es menor o igual a 0, o si el tipo de lado no es válido.

    Se retorna una tupla (opuesto, adyacente, hipotenusa) con los tres lados.
    '''
    if angulo not in PROPORCIONES_APROXIMADAS:
        raise ValueError(
            f"{angulo}° no es un ángulo aproximado. Ángulos válidos: {list(PROPORCIONES_APROXIMADAS)}."
        )
    validar_lados(lado)
    if tipo not in TIPOS_LADO:
        raise ValueError(f"Tipo de lado '{tipo}' no válido. Use uno de: {TIPOS_LADO}.")

    proporcion = PROPORCIONES_APROXIMADAS[angulo]
    k = lado / proporcion[TIPOS_LADO.index(tipo)]
    return tuple(p * k for p in proporcion)