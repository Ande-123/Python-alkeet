#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
# yksi leiviskä on 20 naulaa
#yksi naula on 32 luotia
#yksi luoti on 13,3g

print("Minä muunnan keskiaikaiset mitat kilogrammoiksi ja kiloiksi! Kerro minulle vain kuinka monta leiviskää, nauloja sekä luoteja asiasi painaa.")
leiviska = float(input('Leiviskää: '))
naula = float(input('Naulaa: '))
luoti = float(input('Luoti: '))

leiviska1 = leiviska *20*32*13.3
naula1 = naula *32*13.3
luoti1 = luoti *13.3

yhteensa = leiviska1 + naula1 + luoti1

kg = yhteensa // 1000
g = yhteensa % 1000

print("Massa nykymittojen mukaan:")
print(f"{kg} kilogrammaa sekä noin {g:.2f} grammaa.")