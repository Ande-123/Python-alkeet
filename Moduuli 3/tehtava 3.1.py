#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# #Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha = float(input("Kuhan mitta senttimetreinä: "))


if kuha < 37:
    print(f"Laske kuha takaisin, se on alimittainen {37-kuha} senttimetrin verran")
else:
    print("Se on hyvän kokoinen kuha, voit ottaa sen.")