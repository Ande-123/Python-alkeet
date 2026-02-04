#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

import math
sade = float(input('Mikä on ympyrän halkaisija?:'))
pinta_ala = (sade**2) * math.pi
print("Kun ympyrän halkisija on " + str(sade) + " on silloin kyseisen ympyrän pinta-ala " + str(pinta_ala))