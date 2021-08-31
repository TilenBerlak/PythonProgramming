#Obvezna naloga-------------------------------------------------------------
def preberi(ime_dat):
    datoteka = open(ime_dat,"r").readlines()
    slovar = {}
    for i in datoteka:
        if "CCu" not in i:
            buy = float(i[39:52].replace(",", "."))
            sell = float(i[54:67].replace(",", "."))
            slovar[i[34:37]] = (buy, sell)
    return slovar

def izpisi(tecajnica, valute):
    niz = ""
    for i in valute:
        buy, sell = tecajnica[i]
        niz += "{i}{buy:.>12.4f}{sell:.>12.4f}\n".format(i=i, buy=buy, sell=sell)

    return niz

def zapisi(ime_dat, tecajnica):
    datoteka = open(ime_dat, "w")
    seznam = []
    for i in tecajnica:
        seznam.append(i)
    seznam = sorted(seznam)
    tekst = izpisi(tecajnica, seznam)
    datoteka.write(tekst)
    datoteka.close()

#Dodatna naloga-------------------------------------------------------------
#Funkcija potrebuje nekaj sekund da se normalno izvede!
def preberi_bs():
    import urllib.request

    xml = urllib.request.urlopen("http://www.bsi.si/_data/tecajnice/dtecbs.xml").read().decode("ascii")

    st_vrstic = xml.count("oznaka=")

    slovar = {}

    for i in range(st_vrstic):
        if "oznaka=" in xml:
            index = xml.find("oznaka=")
            start_oznaka = index + 8
            end_oznaka = start_oznaka + 3

            start_sifra = end_oznaka + 14
            end_sifra = start_sifra + 7

            if "<" in xml[start_sifra:end_sifra]:
                slovar[xml[start_oznaka:end_oznaka]] = float(xml[start_sifra:end_sifra - 1])
            else:
                slovar[xml[start_oznaka:end_oznaka]] = float(xml[start_sifra:end_sifra])
            xml = xml[:index] + xml[end_sifra + 4:]

    return slovar


#Testi----------------------------------------------------------------------

import unittest


class TestObvezna(unittest.TestCase):
    def test_preberi(self):
        self.assertEqual(
            preberi("tecajnica.txt"),
            {'BAM': (1.985, 1.919), 'PLN': (4.509, 4.361),
             'SEK': (9.929, 9.609), 'CZK': (27.544, 26.544),
             'NOK': (9.2471, 8.9071), 'AUD': (1.4444, 1.4004),
             'HUF': (315.89, 307.09), 'GBP': (0.8639, 0.8399),
             'HRK': (7.6508, 7.4208), 'RUB': (71.9393, 66.5393),
             'USD': (1.0748, 1.0508), 'MKD': (62.11, 60.29),
             'CHF': (1.0942, 1.0602), 'JPY': (121.83, 118.03),
             'BGN': (1.979, 1.925), 'RSD': (124.94, 121.14),
             'DKK': (7.5521, 7.3281), 'CAD': (1.4528, 1.4048)})

        self.assertEqual(
            preberi("tecajnica2.txt"),
            {'GBP': (0.8639, 0.8399), 'USD': (1.0748, 1.0508)})

    def test_izpisi(self):
        tecajnica = preberi("tecajnica.txt")
        self.assertEqual(
            izpisi(tecajnica, ["GBP", "USD", "RUB", "HRK", "HUF"]),
                   """GBP......0.8639......0.8399
USD......1.0748......1.0508
RUB.....71.9393.....66.5393
HRK......7.6508......7.4208
HUF....315.8900....307.0900
""")

    def test_zapisi(self):
        from random import randint
        import os

        tecajnica = preberi("tecajnica.txt")
        try:
            ime_dat = "test{:05}".format(randint(0, 99999))
            zapisi(ime_dat, tecajnica)
            with open(ime_dat) as tvoj, open("pravilno.txt") as moj:
                self.assertEqual(tvoj.read(), moj.read())
        finally:
            os.remove(ime_dat)

class TestDodatna(unittest.TestCase):
    def test_preberi_bs(self):
        tecajnica = preberi_bs()
        print(set(tecajnica))
        self.assertEqual(
            set(tecajnica),
            {'PLN', 'SEK', 'MXN', 'BGN', 'HUF', 'RUB', 'ILS', 'MYR', 'CAD',
             'BRL', 'SGD', 'USD', 'CZK', 'RON', 'CNY', 'HKD', 'NOK', 'DKK',
             'JPY', 'INR', 'AUD', 'KRW', 'PHP', 'ZAR', 'THB', 'IDR', 'TRY',
             'CHF', 'GBP', 'NZD', 'HRK'})
        self.assertLess(abs(tecajnica["USD"] - 1.06), 0.2)
        self.assertLess(abs(tecajnica["HRK"] - 7.5), 0.2)

if __name__ == "__main__":
    unittest.main()

