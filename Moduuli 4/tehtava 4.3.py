#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.


luvut = []

while True:
    antaa = input("Anna luku, jos annat tyhjän, lopetan:")

    if antaa == "":
        break
    luvut.append(float(antaa))

pienin = min(luvut, default="Ei lukuja")
suurin = max(luvut, default="Ei lukuja")

print(f"Pienin luku on {pienin} ja suurin luku on {suurin}.")
