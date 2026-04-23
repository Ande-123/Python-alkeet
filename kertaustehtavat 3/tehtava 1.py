# Luo sanakirja seuraavilla avaimilla ja arvoilla:


henkilot = {
    "John" : ["John", 30, "Engineer"],
    "Emily" : ["Emily", 25, "Artist"],
    "Anna" : ["Anna", 22, "Student"]}

    # Hae ja tulosta: Johnin nimi ja ikä sekä Emilyn ammatti.

print(f"Johnin nimi: {henkilot['John'][0]}, ikä: {henkilot['John'][1]}")
print(f"Emily on ammatiltaan: {henkilot['Emily'][2]}")

    # Muokkaa sanakirjaa: vaihda Annan ammatiksi "Teacher" ja lisää uusi avain-arvo-pari
    # "James" listalla ["James", 28, "Writer"].

henkilot["Anna"][2] = "Teacher"
henkilot["James"] = ["James", 28, "Writer"]

    # Lisää uusi merkintä: "Sophia", jonka ikä on 35 ja ammatti lääkäri.

henkilot["Sophia"] = ["Sophia", 35, "Doctor"]

    # Poista yksi merkintä: poista "Emily" sanakirjasta.

del henkilot["Emily"]

    #  Tulosta lopullinen sanakirja.

print("Lopullinen sanakirja:")
print(henkilot)
