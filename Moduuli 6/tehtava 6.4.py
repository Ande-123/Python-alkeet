# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def laske_summa(lukulista):
    summa = 0
    for x in lukulista:
        summa += x
    return summa

numerot = [5,10,20,100,40,35,34,62,3,456,36,32,42]
tulos = laske_summa(numerot)

print(f"Listan numeroiden summa on {tulos}")