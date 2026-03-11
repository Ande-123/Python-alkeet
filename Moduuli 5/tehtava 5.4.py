# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
# kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta
# niiden läpikäymiseen.

lista = []

for i in range(5):
    kapu = input("Kerro kaupunki: ")
    lista.append(kapu)

print("Tässä ovat kaikki kaupungit, mitä sanoit:")

for nimi in lista:
    print(nimi)