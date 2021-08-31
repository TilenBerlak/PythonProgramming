# Tu dodajte svoje funkcije

#Ogrevalna naloga----------------------------------------

def prazna(a):
    plosca = []
    for i in range(a):
        plosca.append("")
    return plosca

def je_prazna(plosca):
    for i in plosca:
        if i != "":
            return False
    return True

def v_niz(plosca):
    niz = ""
    for i in plosca:
        if i == "":
            niz += " "
        else:
            niz += i
    return niz

#Obvezna naloga--------------------------------------------

def je_prostor(plosca, kje, dolzina):
    rez = plosca[kje:kje+dolzina+1]

    if len(rez) < dolzina:
        return False

    if kje != 0 and plosca[kje-1] != "":
        return False

    prostor = True
    for i in rez:
        if i != "":
            prostor = False
            return False
    if prostor:
        return True

def postavi(plosca, kje, dolzina, oznaka):
    if je_prostor(plosca, kje, dolzina):
        i = kje
        while(i < kje+dolzina):
            plosca[i] = oznaka
            i += 1
        return True
    else:
        return False

def obstaja(plosca, oznaka):
    obstaja = False
    for i in plosca:
        if i == oznaka:
            obstaja = True
    return obstaja

def vse_oznake(plosca):
    oznake = []
    for i in plosca:
        dodaj = True
        if i != "":
            for j in oznake:
                if j==i:
                    dodaj = False
                    break
            if dodaj:
                oznake.append(i)
    return oznake


def strel(plosca, kje):
    if plosca[kje] == "":
        return 0

    oznaka = plosca[kje]
    plosca[kje] = ""
    for i in plosca:
        if i == oznaka:
            return 1

    if je_prazna(plosca):
        return 3

    niLadje = True
    for i in plosca:
        if i == oznaka and i != "":
            niLadje = False
    else:
        return 2

#Dodatna naloga---------------------------------------------

def razpostavi(n, ladje):
    plosca = []
    i = 0
    while i < n:
        plosca.append("")
        i += 1
    for a in ladje:
        oznaka, dolzina = a
        j = 0
        while j < len(plosca):
            if j != 0 and plosca[j - 1] == "" and plosca[j] == "":
                kje = j
                break
            elif j == 0 and plosca[j] == "":
                kje = j
                break
            j += 1

        if je_prostor(plosca, kje, dolzina):
            i = kje
            while (i < kje + dolzina):
                plosca[i] = oznaka
                i += 1

    return plosca

#Testi--------------------------------------------------------

import unittest

class TestOgrevanje(unittest.TestCase):
    def test_prazna(self):
        self.assertEqual(prazna(1), [''])
        self.assertEqual(prazna(4), ['', '', '', ''])
        p = prazna(100)
        self.assertEqual(len(p), 100)
        self.assertTrue(all(map(''.__eq__, p)))

    def test_je_prazna(self):
        self.assertTrue(je_prazna(['', '', '', '']))
        self.assertTrue(je_prazna(['', '', '', '', '', '' ,'']))
        self.assertFalse(je_prazna(['', '', 'x', '', '', '' ,'']))
        self.assertFalse(je_prazna(['', '', 'a', '', '', '' ,'']))
        self.assertFalse(je_prazna(['x', 'x', 'x', 'x', 'x', 'x' ,'x']))

    def test_v_niz(self):
        self.assertEqual(v_niz(["a"]), "a")
        self.assertEqual(v_niz(["a", "b"]), "ab")
        self.assertEqual(v_niz(["a", "b", "a", "c"]), "abac")

        self.assertEqual(v_niz(["a", "b", "", "c"]), "ab c")
        self.assertEqual(v_niz(['', '', 'a', 'a', 'a', '', 'd', '', '']), "  aaa d  ")
        self.assertEqual(v_niz(prazna(4)), "    ")


class TestObvezna(unittest.TestCase):
    def test_je_prostor(self):
        plosca = ['', '', '', '', '', '', '', '', '', '']
        self.assertTrue(je_prostor(plosca, 1, 3))
        self.assertTrue(je_prostor(plosca, 6, 3))

        self.assertTrue(je_prostor(plosca, 0, 3))
        self.assertTrue(je_prostor(plosca, 7, 3))

        plosca[9] = "a"
        self.assertTrue(je_prostor(plosca, 0, 3))
        self.assertTrue(je_prostor(plosca, 0, 1))
        self.assertTrue(je_prostor(plosca, 7, 1))

        self.assertFalse(je_prostor(plosca, 8, 1))
        self.assertFalse(je_prostor(plosca, 7, 2))

        plosca = ['', '', '']
        self.assertTrue(je_prostor(plosca, 0, 1))
        self.assertTrue(je_prostor(plosca, 0, 2))
        self.assertTrue(je_prostor(plosca, 0, 3))
        self.assertTrue(je_prostor(plosca, 1, 1))
        self.assertTrue(je_prostor(plosca, 1, 2))
        self.assertTrue(je_prostor(plosca, 2, 1))
        self.assertFalse(je_prostor(plosca, 1, 3))

        plosca = ['a', '', '']
        self.assertFalse(je_prostor(plosca, 0, 1))
        self.assertFalse(je_prostor(plosca, 0, 2))
        self.assertFalse(je_prostor(plosca, 0, 3))
        self.assertFalse(je_prostor(plosca, 1, 1))
        self.assertFalse(je_prostor(plosca, 1, 2))
        self.assertTrue(je_prostor(plosca, 2, 1))

        plosca = ['', 'a', '']
        self.assertFalse(je_prostor(plosca, 0, 1))
        self.assertFalse(je_prostor(plosca, 0, 2))
        self.assertFalse(je_prostor(plosca, 0, 3))
        self.assertFalse(je_prostor(plosca, 1, 1))
        self.assertFalse(je_prostor(plosca, 1, 2))
        self.assertFalse(je_prostor(plosca, 2, 1))

        plosca = ['', '', 'a']
        self.assertTrue(je_prostor(plosca, 0, 1))
        self.assertFalse(je_prostor(plosca, 0, 2))
        self.assertFalse(je_prostor(plosca, 0, 3))
        self.assertFalse(je_prostor(plosca, 1, 1))
        self.assertFalse(je_prostor(plosca, 1, 2))
        self.assertFalse(je_prostor(plosca, 2, 1))

    def test_postavi(self):
        plosca = ['', '', '', '', '', '', '', '', '', '']
        self.assertTrue(postavi(plosca, 2, 3, 'x'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', '', '', '', ''])
        self.assertFalse(postavi(plosca, 1, 1, 'y'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', '', '', '', ''])
        self.assertFalse(postavi(plosca, 0, 2, 'y'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', '', '', '', ''])
        self.assertFalse(postavi(plosca, 5, 2, 'y'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', '', '', '', ''])
        self.assertFalse(postavi(plosca, 5, 2, 'y'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', '', '', '', ''])
        self.assertTrue(postavi(plosca, 6, 2, 'y'))
        self.assertEqual(plosca, ['', '', 'x', 'x', 'x', '', 'y', 'y', '', ''])
        self.assertTrue(postavi(plosca, 0, 1, 'a'))
        self.assertEqual(plosca, ['a', '', 'x', 'x', 'x', '', 'y', 'y', '', ''])

    def test_obstaja(self):
        plosca = ['a', '', 'x', 'x', 'x', '', 'y', 'y', '', '']
        self.assertTrue(obstaja(plosca, 'a'))
        self.assertTrue(obstaja(plosca, 'x'))
        self.assertTrue(obstaja(plosca, 'y'))
        self.assertFalse(obstaja(plosca, 'b'))

    def test_vse_oznake(self):
        plosca = ['a', '', 'x', 'x', 'x', '', 'y', 'y', '', '']
        self.assertEqual(set(vse_oznake(plosca)), set("axy"))
        plosca = ['', '', '', 'x', 'x', '', '', '', '', '']
        self.assertEqual(vse_oznake(plosca), ['x'])
        plosca = ['', '', '', '', '', '', '', '']
        self.assertEqual(vse_oznake(plosca), [])

    def test_strel(self):
        plosca = ['a', '', 'x', 'x', 'x', '', 'y', 'y', '', '']
        self.assertEqual(strel(plosca, 3), 1)
        self.assertEqual(plosca, ['a', '', 'x', '', 'x', '', 'y', 'y', '', ''])
        self.assertEqual(strel(plosca, 3), 0)
        self.assertEqual(plosca, ['a', '', 'x', '', 'x', '', 'y', 'y', '', ''])
        self.assertEqual(strel(plosca, 9), 0)
        self.assertEqual(plosca, ['a', '', 'x', '', 'x', '', 'y', 'y', '', ''])
        self.assertEqual(strel(plosca, 2), 1)
        self.assertEqual(plosca, ['a', '', '', '', 'x', '', 'y', 'y', '', ''])
        self.assertEqual(strel(plosca, 7), 1)
        self.assertEqual(plosca, ['a', '', '', '', 'x', '', 'y', '', '', ''])
        self.assertEqual(strel(plosca, 6), 2)
        self.assertEqual(plosca, ['a', '', '', '', 'x', '', '', '', '', ''])
        self.assertEqual(strel(plosca, 2), 0)
        self.assertEqual(plosca, ['a', '', '', '', 'x', '', '', '', '', ''])
        self.assertEqual(strel(plosca, 0), 2)
        self.assertEqual(plosca, ['', '', '', '', 'x', '', '', '', '', ''])
        self.assertEqual(strel(plosca, 4), 3)
        self.assertEqual(plosca, ['', '', '', '', '', '', '', '', '', ''])


class TestDodatna(unittest.TestCase):
    def test_razpostavi(self):
        plosca = razpostavi(10, [('a', 3)])
        s = v_niz(plosca)
        self.assertTrue('aaa' in s)
        self.assertEqual(s.count('a'), 3,
                         "Ladja 'a' mora biti dolga 3")

        ladje = [('a', 2), ('b', 3), ('c', 1)]
        plosca = razpostavi(10, ladje)
        s = v_niz(plosca)
        self.assertEqual(len(plosca), 10)
        for oznaka, dolzina in ladje:
            self.assertTrue(oznaka * dolzina in s)
            self.assertEqual(s.count(oznaka), dolzina,
                             "Ladja '{}' mora biti dolga {}".format(oznaka, dolzina))
        for c, d in zip(plosca, plosca[1:]):
            self.assertFalse(c and d and c != d,
                             "Ladje se ne smejo dotikati")


if __name__ == "__main__":
    unittest.main()
