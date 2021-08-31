#Dodatna naloga: Računalnik ugiba število
from random import randint

x = int(input("Vnesi skrito število: "))
hint = ""
stPoskusov = 0
st = randint(0,100)
najmanjse = 0
najvecje = 100
while hint!="bravo":
    stPoskusov += 1
    print(st,"?")
    hint = input("manj ali več?: ")
    if hint == "manj":
        najvecje = st
        st = int((najmanjse+najvecje)/2)
    elif hint == "več":
        najmanjse = st
        st = int((najmanjse+najvecje)/2)
    elif hint == "bravo":
        print("Potreboval sem", stPoskusov, "poskusov.")
