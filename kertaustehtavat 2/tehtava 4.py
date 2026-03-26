# Kirjoita funktio nimeltä kuusi, joka ottaa yhden argumentin.
# Funktio tulostaa tekstin "Tämä on kuusi!" sekä kuusen,
# jonka koko määräytyy annetun argumentin perusteella.


def kuusi(koko):
    print("Tämä on kuusi!")

    for i in range(1, koko+1):
        valilyonnit = " " * (koko - i)
        tahdet = "*" * (2 * i - 1)
        print(valilyonnit + tahdet)

    print(" " * (koko - 1) + "*")


kuusi(3)
