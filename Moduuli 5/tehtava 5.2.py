# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla
# sort-metodille argumentiksi reverse=True.

print("Anna lukuja, lopetan kun annat tyhjän merkkijonon.")

luvut = []

while True:
    numero = input("Anna luku: ")

    if numero == "":
        break

    else:
        numero = int(numero)
        luvut.append(numero)

print("Tässä ovat viisi suurinta lukuasi:")
luvut.sort(reverse=True)
print(luvut[0:5])