# Kirjoita ohjelma, joka tulostaa kertotaulun käyttäjän antamalle numerolle välillä 1-10.

luku = int(input("Anna luku 1-10 välillä: "))

if luku<=10 and luku>=0:
    print(f"Numeron {luku} kertotaulu on:")
    for i in range(1,11):
        print(f"{luku}x{i} = {i*luku}")



