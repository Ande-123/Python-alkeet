# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
# palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.


def litroiksi(gallonat):
    return gallonat * 3.785

while True:
    x = float(input("Annan bensiinin määrä galloneina (nagatiivinen lopettaa): "))
    if x < 0:
        print("Nyt lopetan!")
        break
    else:
        litrat = litroiksi(x)
        print(f"{x} galloonaa on {litrat:.2f} litraa")
