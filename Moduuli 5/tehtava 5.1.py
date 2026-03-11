# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.


import random


nopat = int(input("Noppien lukumäärä: "))
summa = 0


for i in range(nopat):
    heitto = random.randint(1,6)
    summa += heitto

print(f"Noppien silmälukujen summa: {summa}")