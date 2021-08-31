#Naloga: Računalnik si izmisli število in ga ugiba
#Odstranite komentarje pri print funkcijah, če želite videti kako računalnik ugiba števila
import matplotlib.pyplot as plt #Knjižnica za risanje grafov. Naložil sem jo na OS Windows z uporabo pip install
from random import randint

limit = 100
povprecja = [0,0,0] # tabela za shranjevanje povprečij
a = 0 # spremenljivka pripada tabeli
while limit <= 10000: # ugiba števila med 0-100, 0-1000, 0-10000
    avg = 0
    i = 0
    while i < 100: # 100 krat ugibamo število od 0 do limit
        najmanjse = 0
        najvecje = limit
        x = randint(najmanjse, najvecje) # Računalnik si izmisli število
        #print("x=", x)

        hint = ""
        stPoskusov = 0
        y = randint(najmanjse, najvecje) # Računalnik ugiba število
        staro = y + 1

        while hint != "bravo":
            stPoskusov += 1
            #print(y,"?")
            if y > x:
                hint = "manj"
                #print(hint)
                najvecje = y
                staro = y
                y = int((najmanjse+najvecje)/2)
                if y == staro: y += 1 # V primeru da je skrito število 100, 1000 ali 10000
            elif y < x:
                hint = "več"
                #print(hint)
                najmanjse = y
                staro = y
                y = int((najmanjse+najvecje)/2)
                if y == staro: y += 1 # V primeru da je skrito število 100, 1000 ali 10000
            elif y == x:
                hint = "bravo"
                #print(hint)
                avg += stPoskusov
                #print("Potreboval sem", stPoskusov, "poskusov.")

        i += 1
    print("Povprečno število poskusov za števila od 0 do",limit,":", avg/100)
    povprecja[a] = avg/100 #Shranjevanje povprčja v tabelo
    a += 1
    limit *= 10

#Risanje grafa
plt.bar([100,1000,10000],povprecja)
#plt.plot(povprecja,[100,1000,10000]) #Drugačna vrsta grafa
plt.title("Računalnik ugiba števila")
plt.ylabel("Povprečno število ugibanj")
plt.xlabel("Največje število pri ugibanju")
plt.show()
