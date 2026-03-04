# Kirjoita ohjelma, joka pyytää käyttäjältä sanoja.
# Jos käyttäjä kirjoittaa sanan "loppu", ohjelma tulostaa muodostuneen tarinan ja lopettaa.

tarina = []

print("Kerro tarina sana sanalta, kun sanot ´loppu´ tarina loppuu ja tulostan tarinan.")


while True:

    sana = input("Anna sana lisättäväksi tarinaan: ")

    if sana == "loppu":
        print(" ".join(tarina))
        break
    else:
        tarina.append(sana)

