# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.


import math

def yksikkohinta(halkaisija, hinta):
    sade = (halkaisija/2)/100
    pinta_ala = math.pi * (sade**2)
    return hinta / pinta_ala

print("Ensimmäinen pizza")
d1 = float(input("Halkaisija (cm): "))
p1 = float(input("Hinta: "))

print("Toisen pizza")
d2 = float(input("Halkaisija (cm): "))
p2 = float(input("Hinta: "))

hinta1 = yksikkohinta(d1, p1)
hinta2 = yksikkohinta(d2, p2)

print(f"Ensimmäinen pizza maksaa {hinta1:.2f} €/m^2")
print(f"Toisen pizza maksaa {hinta2:.2f} €/m^2")

if hinta1 > hinta2:
    print("Toinen pizza on kannattavampi.")
elif hinta1 < hinta2:
    print("Ensimmäinen pizza on kannattavampi.")
else:
    print("Pizzat ovat saman arvoisia.")


