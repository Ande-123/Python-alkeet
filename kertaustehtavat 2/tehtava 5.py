# Kirjoita funktio nimeltä suurin_arvo, joka saa kolme argumenttia.
# Funktion tulee palauttaa näistä kolmesta suurin arvo.
# Kysy luvut käyttäjältä input-funktion avulla



def suurin_arvo(a,b,c):
    return max(a,b,c)

num1 = float(input("Anna ensimmäinen luku: "))
num2 = float(input("Anna toinen luku: "))
num3 = float(input("Anna kolmas luku: "))

tulos = suurin_arvo(num1,num2,num3)

print(f"Antamasi lukujen suurin on {tulos}.")
