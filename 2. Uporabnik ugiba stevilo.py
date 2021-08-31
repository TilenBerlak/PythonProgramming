#Obvezna naloga: Uporabnik ugiba število
from random import randint

x = randint(0, 63)
stPoskusov = 0
st = x+1
print("Računalnik si je izmislil število. Ugani ga!")
while st != x:
    st = int(input("Vnesi število: "))
    stPoskusov += 1
    if st > x:
        print("Manj")
    elif st < x:
        print("Več")
    else:
        print("Število si uganil v", stPoskusov, "poskusih!")