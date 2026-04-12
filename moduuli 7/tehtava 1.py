# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.


vuodenajat = ("talvi", "kevät", "kesä", "syksy")

try:
    kuukausi = int(input("Anna kuukauden numero: "))

    if 1<=kuukausi<=12:
        indeksi = (kuukausi % 12) // 3

        valittu_vuodenaika = vuodenajat[indeksi]
        print(f"Kuukautesi vuodenaika on {valittu_vuodenaika}.")
    else:
        print(f"Tuo ei ole mikään kuukausi!")

except ValueError:
    print("Syötä kuukausi numeroina!")