#Strelske vaje
from math import *

print("Strelske vaje!");
v = float(input("Vnesi hitrost izstrelka: "));
kot = float(input("Vnesi kot izstrelka: "));
rad = kot*pi/180 #funkcija sin() potrebuje argument v radianih
g = 9.81;
s = (pow(v,2) * sin(2*rad))/g;
print("Izstrelek bo letel ", s, " metrov");
