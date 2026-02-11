#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
#antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm


print("Muunnan tuumat senttimetreiksi, kunnes annat negatiivisen tuuman")


while True:
    luku = float(input("Tuuma: "))

    if luku < 0:
        print("Nyt lopetan, koska annoit negatiivisen luvun")
        break

    print(luku *2.54)



