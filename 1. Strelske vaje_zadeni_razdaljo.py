#Strelske vaje, zadeni razdaljo
from math import *
from random import *

x = randint(3,10)
print("Strelske vaje!")
print("Izstrelek mora leteti približno ", x, " m.")
zadetek = 0
while(zadetek==0):
    v = int(input("Vnesi hitrost izstrelka: "))
    kot = int(input("Vnesi kot izstrelka: "))
    rad = kot*pi/180 #funkcija sin() potrebuje argument v radianih
    g = 9.81
    s = (pow(v,2) * sin(2*rad))/g
    if(s > (x-0.1) and s < (x+0.1) ): #Približno x metrov
        zadetek = 1
        print("Izstrelek je letel ", s, " metrov.")
        print("Zadeli ste razdaljo ", x, "m!")
    else:
        print("Izstrelek je letel ", s, " metrov.")
        print("Poskusite še enkrat.")
        
    
