# Kirjoita ohjelma, joka pyytää käyttäjää syöttämään arvoja ja lisää ne listaan.
# Jokaisen lisäyksen jälkeen lista tulostetaan kahdella tavalla:
# lisäysjärjestyksessä ja pienimmästä suurimpaan järjestettynä.
# Ohjelma lopettaa, kun käyttäjä syöttää 0.


lista = []

while True:
    syote = int(input("Uusi arvo: "))
    if syote == 0:
        break

    lista.append(syote)
    print(f"Lista nyt: {lista}")
    print(f"Lista järejstyksessä: {sorted(lista)}")
