#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

tunnus = "python"
sala = "rules"

yritys = 0
while yritys < 5:
    yritys += 1
    kayttaja = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if salasana == sala and kayttaja == tunnus:
        print("Tervetuloa!")
        break
    else:
        print("Väärä salasana tai käyttäjätunnus. Yritä uudelleen (max 5 yritystä).")

else:
    print("Pääsy evätty.")