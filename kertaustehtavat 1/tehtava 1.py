#Kirjoita ohjelma keittokauppaa varten: Ohjelma kysyy käyttäjän nimen.
# Jos nimi on jokin muu kuin "Matti", ohjelma kysyy keittoannosten määrän ja tulostaa kokonaishinnan.
#Yhden annoksen hinta on 5,90.


nimi = input("Kerro nimesi:")

if nimi.casefold() != "matti":
    annokset = int(input("Kuinka monta keittoannosta haluat:"))
    print(f"Se tekee {(annokset * 5.9):.2f} euroa.")
else:
    print("Mene pois Matti!")

print("Seuraava kiitos!")

