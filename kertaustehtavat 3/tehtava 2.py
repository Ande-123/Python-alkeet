# Luo sanakirja, jossa oppilaiden nimet ovat avaimina ja listat arvoina.
# Jokaisen listan tulee sisältää: [nimi, vuosiluokka, lempiaine]

oppilaat = {
    "Liisa": ["Liisa", 5, "Matematiikka"],
    "Matti": ["Matti", 3, "Liikunta"],
    "Pekka": ["Pekka", 6, "Historia"]}

    # Hae ja tulosta yhden oppilaan vuosiluokka sekä toisen oppilaan lempiaine.

print(f"Liisan vuosiluokka: {oppilaat['Liisa'][1]}")
print(f"Matin lempiaine: {oppilaat['Matti'][2]}")

    # Muokkaa sanakirjaa vaihtamalla yhden oppilaan lempiaine.

oppilaat["Pekka"][2] = "Biologia"

    # Lisää uusi oppilas sanakirjaan.

oppilaat["Eemil"] = ["Eemil", 1, "Ympäristöoppi"]

    # Poista yksi olemassa oleva oppilas sanakirjasta.

del oppilaat["Matti"]

    # Tulosta päivitetty sanakirja.

print("Päivitetty sanakirja:")
print(oppilaat)

