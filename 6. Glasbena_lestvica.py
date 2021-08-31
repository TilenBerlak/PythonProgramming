
#Obvezna naloga----------------------------------

def prazen_spisek():
    return {}

def poslusam(spisek, pesem):
    if pesem not in spisek:
        spisek[pesem] = 1
    else:
        spisek[pesem] += 1

def predvajanj(spisek, pesem):
    if pesem in spisek and spisek[pesem] > 0:
        return spisek[pesem]
    else:
        return 0

def vseh_pesmi(spisek):
    st_predvajanj = 0
    for i in spisek:
        st_predvajanj += 1
    return st_predvajanj

def vseh_predvajanj(spisek):
    st_predvajanj = 0
    for i in spisek:
        st_predvajanj += spisek[i]
    return st_predvajanj

def najbolj_priljubljena(spisek):
    if len(spisek) > 0:
        max = 0
        naj_priljubljena = ""
        for i in spisek:
            if max < spisek[i]:
                max = spisek[i]
                naj_priljubljena = i
        return naj_priljubljena

def stevilo_skupnih(spisek1, spisek2):
    skupne_pesmi = 0
    for i in spisek1:
        for j in spisek2:
            if i==j:
                skupne_pesmi += 1
    return skupne_pesmi

def velikost_repertoarja(spisek1, spisek2):
    seznam_pesmi = []
    for i in spisek1:
        if i not in seznam_pesmi:
            seznam_pesmi.append(i)
    for i in spisek2:
        if i not in seznam_pesmi:
            seznam_pesmi.append(i)
    return len(seznam_pesmi)

def podobnost(spisek1, spisek2):
    if len(spisek1) and len(spisek2) > 0:
        st_skupnih = stevilo_skupnih(spisek1, spisek2)
        st_vseh = velikost_repertoarja(spisek1, spisek2)
        return st_skupnih/st_vseh
    else:
        return 0


#Dodatna naloga-------------------------------------------

def lestvica(spisek, n):
    if len(spisek) >= n:
        seznam_naj_pesmi = [""] * n
        vrstni_red_st = [0] * n
    else:
        seznam_naj_pesmi = [""] * len(spisek)
        vrstni_red_st = [0] * len(spisek)
    for i, e in spisek.items():
        for index, element in enumerate(vrstni_red_st):
            if e > element:
                x = len(vrstni_red_st) - 2
                while (x >= index):
                    vrstni_red_st[x + 1] = vrstni_red_st[x]
                    seznam_naj_pesmi[x + 1] = seznam_naj_pesmi[x]
                    x -= 1
                vrstni_red_st[index] = e
                seznam_naj_pesmi[index] = i
                break

    for j, e in enumerate(vrstni_red_st):
        if j < len(vrstni_red_st) - 1 and e == vrstni_red_st[j + 1]:
            x = j
            a = e
            while (a == e and x < len(vrstni_red_st)):
                a = vrstni_red_st[x]
                x += 1
            rez = seznam_naj_pesmi[j:x]
            rez.sort()
            b = 0
            y = j
            while (y < x):
                seznam_naj_pesmi[y] = rez[b]
                y += 1
                b += 1
    return seznam_naj_pesmi



#Testi----------------------------------------------------

import unittest


prevodi = [("prazen_spisek", "empty_list"),
           ("poslusam", "play"),
           ("predvajanj", "song_plays"),
           ("vseh_pesmi", "total_songs"),
           ("vseh_predvajanj", "total_plays"),
           ("najbolj_priljubljena", "favourite"),
           ("stevilo_skupnih", "number_of_common"),
           ("velikost_repertoarja", "repertoire_size"),
           ("podobnost", "similarity"),
           ("lestvica", "chart")]
globals().update({slov: globals()[angl]
                  for slov, angl in prevodi if angl in globals()})

class TestObvezna(unittest.TestCase):
    def test_prazen_spisek(self):
        # Preverjamo samo, ali jo lahko pokličemo
        # We only check if the function can be called
        prazen_spisek()

    def test_poslusam_predvajanj(self):
        spisek = prazen_spisek()
        self.assertEqual(predvajanj(spisek, "Red"), 0)

        self.assertIsNone(poslusam(spisek, "Red"))
        self.assertEqual(predvajanj(spisek, "Red"), 1)
        self.assertEqual(predvajanj(spisek, "Yellow Submarine"), 0)

        self.assertIsNone(poslusam(spisek, "Red"))
        self.assertEqual(predvajanj(spisek, "Red"), 2)
        self.assertEqual(predvajanj(spisek, "Yellow Submarine"), 0)
        self.assertIsNone(poslusam(spisek, "Yellow Submarine"))
        self.assertEqual(predvajanj(spisek, "Yellow Submarine"), 1)

    def test_vseh_pesmi_in_predvajanj(self):
        pesmi = ["Brown Sugar", "Red", "Red", "Yellow Submarine",
                 "Purple Rain", "Yellow Submarine", "White Flag", "Red",
                 "White Rabbit", "Brown Sugar"]
        spisek = prazen_spisek()
        for pesem in pesmi:
            poslusam(spisek, pesem)
        self.assertEqual(vseh_pesmi(spisek), 6)
        self.assertEqual(vseh_predvajanj(spisek), 10)

        spisek = prazen_spisek()
        self.assertEqual(vseh_pesmi(spisek), 0)
        self.assertEqual(vseh_predvajanj(spisek), 0)

        for i in range(5):
            poslusam(spisek, "Red")
        self.assertEqual(vseh_pesmi(spisek), 1)
        self.assertEqual(vseh_predvajanj(spisek), 5)

    def test_najbolj_priljubljena(self):
        pesmi = ["Brown Sugar", "Red", "Red", "Yellow Submarine",
                 "Purple Rain", "Yellow Submarine", "White Flag", "Red",
                 "White Rabbit", "Brown Sugar"]
        spisek = prazen_spisek()
        for pesem in pesmi:
            poslusam(spisek, pesem)
        self.assertEqual(najbolj_priljubljena(spisek), "Red")

        spisek = prazen_spisek()
        self.assertIsNone(najbolj_priljubljena(spisek))

        poslusam(spisek, "Red")
        self.assertEqual(najbolj_priljubljena(spisek), "Red")

    def test_skupne_repertoar_podobnost(self):
        pesmi1 = ["Brown Sugar", "Red", "Red", "Yellow Submarine",
                  "Purple Rain", "Yellow Submarine", "White Flag", "Red",
                  "White Rabbit", "Brown Sugar"]
        pesmi2 = ["Yellow Submarine", "Paint It Black",
                  "Purple Rain", "Yellow Submarine"]
        spisek1 = prazen_spisek()
        for pesem in pesmi1:
            poslusam(spisek1, pesem)
        spisek2 = prazen_spisek()
        for pesem in pesmi2:
            poslusam(spisek2, pesem)
        spisek3 = prazen_spisek()
        poslusam(spisek3, "Pretty Fly")
        spisek4 = prazen_spisek()
        poslusam(spisek4, "Red")
        spisek5 = prazen_spisek()

        self.assertEqual(stevilo_skupnih(spisek1, spisek2), 2)
        self.assertEqual(velikost_repertoarja(spisek1, spisek2), 7)
        self.assertAlmostEqual(podobnost(spisek1, spisek2), 2 / 7)

        self.assertEqual(stevilo_skupnih(spisek1, spisek3), 0)
        self.assertEqual(velikost_repertoarja(spisek1, spisek3), 7)
        self.assertAlmostEqual(podobnost(spisek1, spisek3), 0 / 7)

        self.assertEqual(stevilo_skupnih(spisek1, spisek4), 1)
        self.assertEqual(velikost_repertoarja(spisek1, spisek4), 6)
        self.assertAlmostEqual(podobnost(spisek1, spisek4), 1 / 6)

        self.assertEqual(stevilo_skupnih(spisek1, spisek5), 0)
        self.assertEqual(velikost_repertoarja(spisek1, spisek5), 6)
        self.assertAlmostEqual(podobnost(spisek1, spisek5), 0 / 6)

        self.assertEqual(stevilo_skupnih(spisek1, spisek1), 6)
        self.assertEqual(velikost_repertoarja(spisek1, spisek1), 6)
        self.assertAlmostEqual(podobnost(spisek1, spisek1), 6 / 6)

        self.assertEqual(stevilo_skupnih(spisek3, spisek3), 1)
        self.assertEqual(velikost_repertoarja(spisek3, spisek3), 1)
        self.assertAlmostEqual(podobnost(spisek3, spisek3), 1)

        self.assertEqual(stevilo_skupnih(spisek5, spisek5), 0)
        self.assertEqual(velikost_repertoarja(spisek5, spisek5), 0)
        self.assertAlmostEqual(podobnost(spisek5, spisek5), 0)

class TestDodatna(unittest.TestCase):
    def test_lestvica(self):
        pesmi1 = ["Brown Sugar", "Red", "Red", "Yellow Submarine",
                  "Purple Rain", "Yellow Submarine", "White Flag", "Red",
                  "White Rabbit", "Brown Sugar", "Red", "Yellow Submarine"]
        spisek1 = prazen_spisek()
        for pesem in pesmi1:
            poslusam(spisek1, pesem)
        spisek2 = prazen_spisek()
        poslusam(spisek2, "Red")
        spisek3 = prazen_spisek()

        self.assertEqual(lestvica(spisek1, 3),
                         ["Red", "Yellow Submarine", "Brown Sugar"])
        self.assertEqual(lestvica(spisek1, 1), ["Red"])
        self.assertEqual(lestvica(spisek1, 6),
                         ["Red", "Yellow Submarine", "Brown Sugar",
                          "Purple Rain", "White Flag", "White Rabbit"])
        self.assertEqual(lestvica(spisek1, 10),
                         ["Red", "Yellow Submarine", "Brown Sugar",
                          "Purple Rain", "White Flag", "White Rabbit"])
        self.assertEqual(lestvica(spisek1, 0), [])

        self.assertEqual(lestvica(spisek2, 1), ["Red"])
        self.assertEqual(lestvica(spisek2, 3), ["Red"])
        self.assertEqual(lestvica(spisek2, 0), [])

        self.assertEqual(lestvica(spisek3, 3), [])
        self.assertEqual(lestvica(spisek3, 0), [])


if __name__ == "__main__":
    unittest.main()
