import math
from validaciones import validar_lados

# Proporciones (cateto opuesto, cateto adyacente, hipotenusa) para cada ángulo agudo.
PROPORCIONES_NOTABLES = {
    15: (math.sqrt(6) - math.sqrt(2), math.sqrt(6) + math.sqrt(2), 4),
    30: (1, math.sqrt(3), 2),
    45: (1, 1, math.sqrt(2)),
    60: (math.sqrt(3), 1, 2),
    75: (math.sqrt(6) + math.sqrt(2), math.sqrt(6) - math.sqrt(2), 4),
}

TIPOS_LADO = ("opuesto", "adyacente", "hipotenusa")


def triangulo_notable(angulo, lado, tipo):
    '''
    Se recibe un ángulo agudo notable de un triángulo rectángulo y la longitud
    de uno de sus lados.
    angulo: ángulo agudo en grados (15, 30, 45, 60 o 75)
    lado: longitud del lado conocido
    tipo: qué lado es, respecto al ángulo: "opuesto", "adyacente" o "hipotenusa"

    Formula: cada ángulo notable tiene lados en una proporción fija
             (opuesto : adyacente : hipotenusa), por ejemplo
             30° -> 1 : √3 : 2      45° -> 1 : 1 : √2      60° -> √3 : 1 : 2
             Si el lado conocido equivale a p partes, cada parte mide k = lado / p,
             y los demás lados se obtienen multiplicando su proporción por k.

    Se lanza ValueError si el ángulo no es notable, si el lado es menor o
    igual a 0, o si el tipo de lado no es válido.

    Se retorna una tupla (opuesto, adyacente, hipotenusa) con los tres lados.
    '''
    if angulo not in PROPORCIONES_NOTABLES:
        raise ValueError(
            f"{angulo}° no es un ángulo notable. Ángulos válidos: {list(PROPORCIONES_NOTABLES)}."
        )
    validar_lados(lado)
    if tipo not in TIPOS_LADO:
        raise ValueError(f"Tipo de lado '{tipo}' no válido. Use uno de: {TIPOS_LADO}.")

    proporcion = PROPORCIONES_NOTABLES[angulo]
    k = lado / proporcion[TIPOS_LADO.index(tipo)]
    return tuple(p * k for p in proporcion)