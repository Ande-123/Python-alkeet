#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
luku = random.randint(1, 10)
print("Arvaa lukua 1-10")
while True:
    arvaus = int(input("Arvaa:"))
    if arvaus == luku:
        break
    elif arvaus < luku:
        print("Arvaa isompaa lukua")
    else:
        print("Arvaa pienempää lukua")

print("Arvasit oikein")

