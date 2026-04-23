# Koordinaattipisteet ja etäisyys

import math

    # Luo funktio create_point(x, y), joka palauttaa pisteen monikko-muodossa (x, y).

def create_point(x, y):
    return (x, y)

    # Luo kaksi pistettä käyttämällä funktiota ja kysymällä arvot käyttäjältä.

x1 = float(input("Anna ensimmäisen pisteen x: "))
y1 = float(input("Anna ensimmäisen pisteen y: "))
piste1 = create_point(x1, y1)

x2 = float(input("Anna toisen pisteen x: "))
y2 = float(input("Anna toisen pisteen y: "))
piste2 = create_point(x2, y2)

    # Luo funktio distance(p1, p2), joka laskee kahden pisteen välisen etäisyyden

def distance(p1, p2):

    d = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    return d

    # Kutsu distance-funktiota ja tulosta pisteiden välinen etäisyys.
    # Pyöristä etäisyys kahden desimaalin tarkkuuteen käyttäen formatointia.

etaisyys = distance(piste1, piste2)

print(f"Pisteiden välinen etäisyys on: {etaisyys:.2f}")