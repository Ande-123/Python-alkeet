# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.


lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - syötä uusi lentoasema")
    print("2 - hae lentoaseman nimeä")
    print("0 - lopeta")

    valinta = int(input("Valinta: "))

    if valinta == 1:
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} on tallennettu.")

    elif valinta == 2:
        icao = input("Anna haettava ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print("ICAO-koodia ei löytynyt")

    elif valinta == 0:
        print("Kiitos ja näkemiin!")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")