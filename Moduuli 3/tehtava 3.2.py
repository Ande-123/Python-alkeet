#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
# ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.

#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.


hytti = input("Anna hyttiluokkasi: ").upper()

if hytti == "LUX":
    print("Hyttisi on parvekkellinen hytti yläkannella.")
elif hytti == "A":
    print("Hyttisi on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
    print("Hyttisi on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print("Hyttisi on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

