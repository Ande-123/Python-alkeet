#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

num1 = random.randint(1,9)
num2 = random.randint(1,9)
num3 = random.randint(1,9)

num4 = random.randint(1,6)
num5 = random.randint(1,6)
num6 = random.randint(1,6)
num7 = random.randint(1,6)



print("Tämä ohjelma arpoo sinulle kolmenumeroisen (numerot 0-9) sekä nelinumeroisen koodin (numerot 1-6)")

print(f"Tässä on kolmenumeroinen koodi: {num1}{num2}{num3}")
print(f"Tässä on nelinumeroinen koodi: {num4}{num5}{num6}{num7}")