#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaislukuja. Jos luku on pienempi kuin nolla,
# ohjelma tulostaa viestin "Virheellinen numero". Jos luku on suurempi kuin nolla,
# ohjelma tulostaa luvun neliöjuuren Pythonin sqrt-funktiolla. Molemmissa tapauksissa
# ohjelma kysyy sen jälkeen uutta lukua.

from math import sqrt

while True:
    luku = int(input("Anna kokonaisluku: "))
    if luku == 0:
        print("Lopetetaan")
        break
    elif luku < 0:
        print("Virheellinen numero!")
    else:
        print(f"Luvun neliöjuuri on {sqrt(luku)}")