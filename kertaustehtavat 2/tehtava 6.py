#  Päivitä laskin.py -tiedostosi (esimerkki löytyy OMA:sta, dokumentit-kansiosta) niin,
# että laskutoimitukset suoritetaan niitä vastaavilla funktioilla. Määrittele funktio itse.



def summa(a,b):
    return a+b
def erotus(a,b):
    return a-b
def tulo(a,b):
    return a*b
def osamaara(a,b):
    return a/b

def laskin():
    print("Toiminnot: A=summa, B=erotus, C=tulo, D=osamaara")
    valinta = input("Valitse toiminto: ")

    num1 = int(input("Valitse ensimmäinen luku: "))
    num2 = int(input("Valitse toinen luku:"))

    if valinta == "A":
        print(f"Tulos: ", summa(num1,num2))
    elif valinta == "B":
        print(f"Tulos: ", erotus(num1,num2))
    elif valinta == "C":
        print(f"Tulos: ", tulo(num1,num2))
    elif valinta == "D":
        print(f"Tulos: ", osamaara(num1,num2))

    else:
        print(f"Virheellinen valinta!")

laskin()

