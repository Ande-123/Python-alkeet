# Kirjoita ohjelma, joka kysyy tuntipalkan, tehdyt tunnit ja viikonpäivän.
# Ohjelma tulostaa päiväpalkan, joka on tuntipalkka kerrottuna tehdyillä tunneilla,
# paitsi sunnuntaina, jolloin tuntipalkka on kaksinkertainen.


tuntipalkka = int(input("Tuntipalkka: "))
tunnit = int(input("Tehdyt tunnit: "))
paiva = input("Viikonpäivä: ")

if paiva == "sunnuntai":
    print(f"Päivän palkkasi on {tunnit*tuntipalkka*2}.")
else:
    print(f"Päivän palkkasi on {tunnit*tuntipalkka}.")

