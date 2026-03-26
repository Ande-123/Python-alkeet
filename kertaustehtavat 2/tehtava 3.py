# Kirjoita ohjelma, joka laskee, kuinka monessa sanassa listassa on enemmän kuin 5 kirjainta.
# Luo lista itse ja käytä len()-funktiota sanojen pituuden tarkistamiseen.


lista = ["omena", "kaneli", "pupu", "sateenvarjo", "porkkana", "sateenkaari", "huivi"]

pitka_sana = 0

for sana in lista:
    if len(sana)>5:
        pitka_sana+=1

print(f"Listan sanoista {pitka_sana}:ssa/ssä sanassa on enemmän kuin 5 kirjainta")
