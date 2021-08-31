#Hrček na kolesu

#Obvezna naloga------------------------------------------------------

def v_seznam(s):
    if s != "":
        s = s.split("; ")
        i = 0
        while i < len(s):
            s[i] = s[i].replace(",", ".")
            s[i] = float(s[i])
            i += 1
        return s
    else:
        s = s.split()
        return s

def v_niz(s):
    niz = ""
    x = 0
    while x < len(s):
        if x == len(s)-1:
            niz += str(s[x])
        else:
            niz += str(s[x]) + "; "
        i = 0
        while i < len(niz):
            if niz[i] == ".":
               niz = niz.replace(".", ",")
            i += 1
        x += 1
    return niz

def oznaci_veljavne(s):
    seznam = []
    for i in s:
        value = True
        for j in s:
            if abs(i-j) <= 0.1 and i != j:
                value = False
                break
        seznam.append(value)
    return seznam

def veljavne(s):
    seznam = []
    for i in s:
        value = True
        for j in s:
            if abs(i-j) <= 0.1 and i != j:
                value = False
                break
        if value:
            seznam.append(i)
    return seznam

def brez_napacnih_casov(s):
    max = s[0]
    seznam = [max]
    for i in s:
        if max < i:
            max = i
            seznam.append(max)
    return seznam

#Dodatna naloga------------------------------------------------------------------

def odstrani_neveljavne(s):
    seznam_neveljavnih = []
    i = 0
    while i < len(s):
        for j in s:
            if abs(s[i]-j) <= 0.1 and s[i] != j:
                seznam_neveljavnih.append(s[i])
                break
        i += 1
    for x in seznam_neveljavnih:
        s.remove(x)

def najv_hitrost(s, o):
    pravilne = veljavne(s)
    i = 0
    if len(pravilne) >= 2:
        while i < len(pravilne):
            if len(pravilne) == 2:
                i = 0
                if abs(pravilne[i]-pravilne[i+1]) > 2.0:
                    pravilne = []
                    break
            if i != len(pravilne)-1 and abs(pravilne[i]-pravilne[i+1]) > 2.0 and abs(pravilne[i]-pravilne[i-1]) > 2.0:
                pravilne.remove(pravilne[i])
            i += 1
    if len(pravilne) >= 2:
        najkrajsi_cas = 100
        i = 0
        while i < len(pravilne)-1:
            if najkrajsi_cas > abs(pravilne[i]-pravilne[i+1]) and i != len(pravilne)-1:
                najkrajsi_cas = abs(pravilne[i]-pravilne[i+1])
            i += 1
        max_hitrost = o/najkrajsi_cas
        return max_hitrost


def na_kolesu(s):
    pravilne = veljavne(s)
    print(pravilne)
    i = 0
    if len(pravilne) >= 2:
        while i < len(pravilne):
            if len(pravilne) == 2:
                i = 0
                if abs(pravilne[i] - pravilne[i + 1]) > 2.0:
                    pravilne = []
                    break
            if i != len(pravilne) - 1 and abs(pravilne[i] - pravilne[i + 1]) > 2.0 and abs(
                            pravilne[i] - pravilne[i - 1]) > 2.0:
                pravilne.remove(pravilne[i])
            i += 1
    print(pravilne)
    if len(pravilne) >= 2:
        vsota = 0
        i = 0
        while i < len(pravilne) - 1:
            if abs(pravilne[i]-pravilne[i+1]) < 2.0:
                vsota += abs(pravilne[i] - pravilne[i + 1])
            i += 1
        return vsota

#Testi--------------------------------------

import unittest
class TestObvezna(unittest.TestCase):
    def test_v_seznam(self):
        t = v_seznam("5,180; 5,907; 6,632; 7,215")
        self.assertEqual(len(t), 4)
        for e, f in zip(t, [5.180, 5.907, 6.632, 7.215]):
            self.assertAlmostEqual(e, f)

        t = v_seznam("5,180")
        self.assertEqual(len(t), 1)
        for e, f in zip(t, [5.180]):
            self.assertAlmostEqual(e, f)

        self.assertEqual(v_seznam(""), [])

    def test_v_niz(self):
        self.assertEqual(v_niz([123, 123.75, 124.5]), "123; 123,75; 124,5")
        self.assertEqual(v_niz([123.75]), "123,75")
        self.assertEqual(v_niz([]), "")


    def test_oznaci_veljavne(self):
        self.assertEqual(oznaci_veljavne([5.18, 5.907, 6.632, 7.215]), [True] * 4)
        self.assertEqual(oznaci_veljavne([132.3, 132.94]), [True] * 2)
        self.assertEqual(oznaci_veljavne([183.12]), [True])
        self.assertEqual(oznaci_veljavne([205.134, 205.182, 205.190, 205.207]), [False] * 4)
        self.assertEqual(oznaci_veljavne([308.412, 308.416]), [False] * 2)

        self.assertEqual(oznaci_veljavne([205.134, 205.182, 205.190, 205.207,
                                          250.13, 250.83, 251.6,
                                          308.412, 308.416]),
                         [False] * 4 + [True] * 3 + [False] * 2)

        self.assertEqual(oznaci_veljavne([205.134, 205.182, 308.416]),
                         [False] * 2 + [True])

        self.assertEqual(oznaci_veljavne([205.134, 205.182, 308.416, 308.999]),
                         [False] * 2 + [True] * 2)

        self.assertEqual(oznaci_veljavne([100, 100.8, 205.134, 205.182, 308.416, 308.999]),
                         [True] * 2 + [False] * 2 + [True] * 2)

        self.assertEqual(oznaci_veljavne([100, 100.8, 205.134, 205.182]),
                         [True] * 2 + [False] * 2)

        self.assertEqual(oznaci_veljavne([100,
                                          205.134, 205.182, 205.190, 205.207,
                                          250.13, 250.83, 251.6,
                                          308.412, 308.416]),
                         [True] + [False] * 4 + [True] * 3 + [False] * 2)

        self.assertEqual(oznaci_veljavne([100,
                                          205.134, 205.182, 205.190, 205.207,
                                          250.13, 250.83, 251.6,
                                          308.412, 308.416,
                                          500]),
                         [True] + [False] * 4 + [True] * 3 + [False] * 2 + [True])

        self.assertSequenceEqual(oznaci_veljavne([
            5.18, 5.907, 6.632, 7.215,
            132.3, 132.94,
            183.12,
            205.134, 205.182, 205.190, 205.207,
            308.412, 308.416,
            512.73, 513.20, 513.65,
            918.2, 918.73]),
        [True] * 4 + [True] * 2 + [True] + [False] * 4 + [False] * 2 + [True] * 3 + [True] * 2)

    def test_veljavne(self):
        self.assertEqual(veljavne([5.18, 5.907, 6.632, 7.215]), [5.18, 5.907, 6.632, 7.215])
        self.assertEqual(veljavne([132.3, 132.94]), [132.3, 132.94])
        self.assertEqual(veljavne([183.12]), [183.12])
        self.assertEqual(veljavne([205.134, 205.182, 205.190, 205.207]), [])
        self.assertEqual(veljavne([308.412, 308.416]), [])
        self.assertEqual(veljavne([205.134, 205.182, 205.190, 205.207,
                                   250.13, 250.83, 251.6,
                                   308.412, 308.416]),
                         [250.13, 250.83, 251.6])
        self.assertEqual(veljavne([205.134, 205.182, 308.416]), [308.416])
        self.assertEqual(veljavne([205.134, 205.182, 308.416, 308.999]),
                                  [308.416, 308.999])
        self.assertEqual(veljavne([100, 100.8, 205.134, 205.182, 308.416, 308.999]),
                         [100, 100.8, 308.416, 308.999])
        self.assertEqual(veljavne([100, 100.8, 205.134, 205.182]), [100, 100.8])
        self.assertEqual(veljavne([100,
                                   205.134, 205.182, 205.190, 205.207,
                                   250.13, 250.83, 251.6,
                                   308.412, 308.416]),
                         [100,
                          250.13, 250.83, 251.6])
        self.assertEqual(veljavne([100,
                                   205.134, 205.182, 205.190, 205.207,
                                   250.13, 250.83, 251.6,
                                   308.412, 308.416,
                                   500]),
                         [100,
                          250.13, 250.83, 251.6,
                          500])
        self.assertSequenceEqual(veljavne([5.18, 5.907, 6.632, 7.215,
                                           132.3, 132.94,
                                           183.12,
                                           205.134, 205.182, 205.190, 205.207,
                                           308.412, 308.416,
                                           512.73, 513.20, 513.65,
                                           918.2, 918.73]),
                                 [5.18, 5.907, 6.632, 7.215,
                                  132.3, 132.94,
                                  183.12,
                                  512.73, 513.20, 513.65,
                                  918.2, 918.73])

    def test_brez_napacnih_casov(self):
        self.assertEqual(brez_napacnih_casov([1, 12, 33]), [1, 12, 33])
        self.assertEqual(brez_napacnih_casov([1, 12]), [1, 12])
        self.assertEqual(brez_napacnih_casov([12]), [12])

        self.assertEqual(brez_napacnih_casov([1, 20, 10, 30]), [1, 20, 30])
        self.assertEqual(brez_napacnih_casov([5, 20, 10, 5, 1, 30]), [5, 20, 30])
        self.assertEqual(brez_napacnih_casov([5, 20, 10, 15, 30]), [5, 20, 30])
        self.assertEqual(brez_napacnih_casov([5, 20, 10, 15]), [5, 20])

class TestDodatna(unittest.TestCase):
    def test_odstrani_neveljavne(self):
        t = [5.18, 5.907, 6.632, 7.215]
        self.assertIsNone(odstrani_neveljavne(t))
        self.assertEqual(t, [5.18, 5.907, 6.632, 7.215])

        t = [123]
        self.assertIsNone(odstrani_neveljavne(t))
        self.assertEqual(t, [123])

        t = [205.134, 205.182, 205.190, 205.207]
        self.assertIsNone(odstrani_neveljavne(t))
        self.assertEqual(t, [])

        t = [308.412, 308.416]
        self.assertIsNone(odstrani_neveljavne(t))
        self.assertEqual(t, [])

        t = [205.134, 205.182, 205.190, 205.207,
             250.13, 250.83, 251.6,
             308.412, 308.416]
        self.assertIsNone(odstrani_neveljavne(t))
        self.assertEqual(t, [250.13, 250.83, 251.6])

        t = [5.18, 5.907, 6.632, 7.215,
             132.3, 132.94,
             183.12,
             205.134, 205.182, 205.190, 205.207,
             308.412, 308.416,
             512.73, 513.20, 513.65,
             918.2, 918.73]
        self.assertIsNone(odstrani_neveljavne(t))
        self.assertEqual(t, [5.18, 5.907, 6.632, 7.215,
                             132.3, 132.94,
                             183.12,
                             512.73, 513.20, 513.65,
                             918.2, 918.73])


    def test_najv_hitrost(self):
        self.assertAlmostEqual(najv_hitrost([5.18, 5.907, 6.632, 7.215,
                                             132.3, 132.94,
                                             183.12,
                                             205.134, 205.182, 205.190, 205.207,
                                             308.412, 308.416,
                                             512.73, 513.20, 513.65,
                                             918.2, 918.73], 45),
                               100)
        self.assertAlmostEqual(najv_hitrost([24, 60,
                                             205.134, 205.182, 205.190, 205.207,
                                             512.73, 513.20, 513.65], 45),
                               100)
        self.assertIsNone(najv_hitrost([24, 60, 205, 205.134, 205.140], 45))
        self.assertIsNone(najv_hitrost([205.134, 205.182, 205.190, 205.207,],
                                       45))
        self.assertIsNone(najv_hitrost([182.12,
                                        205.134, 205.182, 205.190, 205.207,],
                                       45))

    def test_na_kolesu(self):
        self.assertAlmostEqual(na_kolesu([5.18, 5.907, 6.632, 7.18]), 2)
        self.assertAlmostEqual(na_kolesu([5.18, 5.907, 6.632, 7.18,
                                          205.134, 205.182, 205.190, 205.207]),
                               2)
        self.assertAlmostEqual(na_kolesu([5.18, 5.907, 6.632, 7.18,
                                          182.5,
                                          205.134, 205.182, 205.190, 205.207]),
                               2)
        self.assertAlmostEqual(na_kolesu([5.18, 5.907, 6.632, 7.18,
                                          182.5, 183,
                                          205.134, 205.182, 205.190, 205.207]),
                               2.5)

if __name__ == "__main__":
    unittest.main()

