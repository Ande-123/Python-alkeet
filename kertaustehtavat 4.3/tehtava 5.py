# Kirjoita Laskin-ohjelma. Käyttäjän tulisi voida tehdä laskutoimituksia, kuten yhteen- ja
# vähennyslasku, kertolasku sekä jakolasku. Käyttäjän pitäisi myös pystyä lopettamaan
# ohjelma. Kun käyttäjä valitsee laskutoimituksen, laskin kysyy käyttäjältä kaksi lukua ja
# suorittaa pyydetyn laskun. Sen jälkeen ohjelma kysyy uudelleen, mitä käyttäjä haluaa
# tehdä. Käytä while-looppia ja if-elif-else rakennetta.


print("Syötä haluamasi laskutoimituksen perässä oleva luku ja lopeta syöttämällä 5")

while True:

    lasku = int(input("Yhteenlasku(1), vähennyslasku(2), kertolasku(3) ja jakolasku(4): "))
    if lasku == 5:
        print("Nyt lopetan!")
        break
    elif lasku == 1:
        A = int(input("Ensimmäinen luku: "))
        B = int(input("Toinen luku: "))
        print(f"Lukujesi summa on {A+B}")

    elif lasku == 2:
        A = int(input("Ensimmäinen luku: "))
        B = int(input("Toinen luku: "))
        print(f"Lukujesi erotus on {A-B}")

    elif lasku == 3:
        A = int(input("Ensimmäinen luku: "))
        B = int(input("Toinen luku: "))
        print(f"Lukujesi tulo on {A*B}")

    elif lasku == 4:
        A = int(input("Ensimmäinen luku: "))
        B = int(input("Toinen luku: "))
        print(f"Lukujesi osamäärä on {A/B}")

    else:
        print("Sinä et osaa noudattaa ohjeita, uh noh.")