# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan
# nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.


import random

x = int(input("Kuinka monta tahkoa on nopassasi?: "))

def heitto():
    return random.randint(0,x)

tulos = 0

while tulos != x:
    tulos = heitto()
    print (f"Nopasta tuli {tulos}")

