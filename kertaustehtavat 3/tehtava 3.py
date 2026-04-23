# Luo sanakirja nimeltä kirjasto, jossa avaimina ovat kirjojen nimet (merkkijonoja) ja arvoina
# listat, jotka sisältävät seuraavat tiedot: [kirjoittaja, julkaisuvuosi, genre]

kirjasto = {
    "Sinuhe egyptiläinen": ["Mika Waltari", 1945, "Historiallinen romaani"],
    "Tuntematon sotilas": ["Väinö Linna", 1954, "Sotaromaani"],
    "Kalevala": ["Elias Lönnrot", 1835, "Eepos"]}

    # Hae ja tulosta yhden kirjan kirjoittaja sekä toisen kirjan genre.

print(f"Sinuhen kirjoittaja: {kirjasto['Sinuhe egyptiläinen']}")
print(f"Kalevalan genre: {kirjasto['Kalevala']}")

    # Muokkaa: vaihda yhden kirjan genre.

kirjasto["Tuntematon sotilas"] = ("Liian pitkä kirja")

    # Lisää uusi kirja sanakirjaan.

kirjasto["Yksi meistä valehtelee"] = ["Karen M. McManus", 2017, "Jännäri"]

    # Poista yksi olemassa oleva kirja sanakirjasta.

del kirjasto["Kalevala"]

    # Tulosta päivitetty sanakirja.

print("Päivitetty kirjasto:")
print(kirjasto)
