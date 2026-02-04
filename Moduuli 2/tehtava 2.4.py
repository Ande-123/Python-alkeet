#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
#Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

print("Anna yhteensä kolme kokonaislukua 0 ja 100 välillä")

numero1 = int(input('Ensimmäinen luku:'))
numero2 = int(input('Toinen luku:'))
numero3 = int(input('Kolmas luku:'))

summa = numero1 + numero2 + numero3
tulo = numero1 * numero2 * numero3
keskiarvo = (numero1 + numero2 + numero3) /3

print("Lukujesi summa on " + str(summa)+ ", tulo on " + str(tulo)+ ", keskiarvo on " +str(keskiarvo))
