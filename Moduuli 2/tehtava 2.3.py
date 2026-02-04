#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
#Ohjelma tulostaa suorakulmion piirin ja pinta-alan.

import math
kanta = float(input('Mikä on suorakulmion kanta?:'))
korkeus = float(input('Mikä on suorakulmion korkeus?:'))
piiri = (kanta*2)+(korkeus)*2
pinta_ala = kanta*korkeus

print("Suorakulmiosi "+str(kanta)+" x "+str(korkeus)+" piiri on "+str(piiri)+"ja pinta-ala on "+str(pinta_ala))

