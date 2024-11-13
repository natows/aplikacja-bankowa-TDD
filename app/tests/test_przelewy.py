import unittest

from ..Konto import Konto
from ..konto_firmowe import KontoFirma

class Przelewy(unittest.TestCase):
    name = 'Dariusz'
    nazwisko = "Januszewski"
    pesel = "042823011111"
    nazwa="spolka sp. z.o.o"
    nip = 1234567890
    
    def test_inTransfer(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, None)
        konto.inTransfer(1500)
        self.assertEqual(konto.saldo, 1500, "Przelew nie przyszedl")
    def test_outTransfer_srodki_sa(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, None)
        konto.saldo=500
        konto.outTransfer(200)
        self.assertEqual(konto.saldo, 300, "Przelew nie przeszedl")
    def test_outTransfer_srodkow_brak(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, None)
        konto.outTransfer(200)
        self.assertEqual(konto.saldo, 0, "Przelew nie przeszedl")  
    def test_express_srodki_sa(self):
        konto=Konto(self.name, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.expressOutTransfer(100)
        self.assertEqual(konto.saldo, 399, "saldo po przelewie sie nie zgadza")
    def test_express_srodkow_brak(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, None)
        konto.expressOutTransfer(100)
        self.assertEqual(konto.saldo, 0, "saldo po przelewie sie nie zgadza")
    def test_Konto_express_srodkow_rowno(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, "PROM_XYZ")
        konto.expressOutTransfer(50)
        self.assertEqual(konto.saldo, -1, "saldo po przelewie sie nie zgadza")

    #testy firmy
    def test_firma_przelew_przychodzacy(self):
        konto=KontoFirma(self.nazwa, self.nip)
        konto.inTransfer(100)
        self.assertEqual(konto.saldo, 100, "Saldo si enie zgadza")
    def test_firma_przelew_wychodzacy_udany(self):
        konto=KontoFirma(self.nazwa, self.nip)
        konto.saldo=150
        konto.outTransfer(100)
        self.assertEqual(konto.saldo, 50, "Saldo si enie zgadza")
    def test_firma_przelew_wychodzacy_nieudany(self):
        konto=KontoFirma(self.nazwa, self.nip)
        konto.outTransfer(100)
        self.assertEqual(konto.saldo, 0, "Saldo sie nie zgadza")
    def test_Firma__express_srodki_sa(self):
        konto=KontoFirma(self.nazwa, self.nip)
        konto.saldo=100
        konto.expressOutTransfer(50)
        self.assertEqual(konto.saldo, 45, "saldo po przelewie sie nie zgadza")
    def test_Firma__express_srodkow_brak(self):
        konto=KontoFirma(self.nazwa, self.nip)
        konto.saldo=100
        konto.expressOutTransfer(200)
        self.assertEqual(konto.saldo, 100, "saldo po przelewie sie nie zgadza")
    def test_Firma__express_srodki_rowno(self):
        konto=KontoFirma(self.nazwa, self.nip)
        konto.saldo=100
        konto.expressOutTransfer(100)
        self.assertEqual(konto.saldo, -5, "saldo po przelewie sie nie zgadza")

    #test historii przelewow
    def test_konto(self):
        konto=Konto(self.name,self.nazwisko,self.pesel)
        konto.inTransfer(500)
        konto.outTransfer(150)
        konto.expressOutTransfer(250)
        self.assertEqual(konto.history, [500,-150,-250,-1], "history sie nie zgadza")
    def test_konto_firmowe(self):
        konto=KontoFirma(self.nazwa, self.nip)
        konto.inTransfer(500)
        konto.outTransfer(150)
        konto.expressOutTransfer(250)
        self.assertEqual(konto.history, [500,-150,-250,-5], "history sie nie zgadza")








        