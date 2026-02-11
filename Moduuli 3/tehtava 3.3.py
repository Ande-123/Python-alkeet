#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Oletko biologisesti mies (M) vai nainen (N): ").upper()
hemo = int(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "M" and hemo < 134:
    print("Hemoglobiiniarvosi ovat liian matalat.")
elif sukupuoli == "M" and hemo > 195:
    print("Hemoglobiiniarvosi ovat korkeat.")
elif sukupuoli == "N" and hemo < 117:
    print("Hemoglobiiniarvosi ovat matalat.")
elif sukupuoli == "N" and hemo > 175:
    print("Hemoglobiiniarvosi ovat korkeat.")
elif sukupuoli != "N" or "M":
    print("En tunnistanut sukupuoltasi.")
else:
    print("Hemoglobiiniarvosi ovat normaalit.")