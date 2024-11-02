import unittest

from ..Konto import Konto
from ..konto_firmowe import KontoFirma

class Przelewy(unittest.TestCase):
    name = 'Dariusz'
    nazwisko = "Januszewski"
    pesel = "042823011111"
    nazwa="gowno sp. z.o.o"
    
    def test_przelew_przychodzacy(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, None)
        konto.inTransfer(1500)
        self.assertEqual(konto.saldo, 1500, "Przelew nie przyszedl")
    def test_przelew_wychodzący_wystrczajaco_srodkow(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, None)
        konto.saldo=500
        konto.outTransfer(200)
        self.assertEqual(konto.saldo, 300, "Przelew nie przeszedl")
    def test_przelew_wychodzacy_niewystarczajaco(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, None)
        konto.outTransfer(200)
        self.assertEqual(konto.saldo, 0, "Przelew nie przeszedl")
    def test_firma_nip_dobry(self):
        nip=1234567890
        konto=KontoFirma(self.nazwa, nip, 0)
        self.assertEqual(konto.nip, nip, "Nip niepoprawny")
    def test_firma_nip_zakrotki(self):
        nip=234
        konto=KontoFirma(self.nazwa, nip, 0)
        self.assertEqual(konto.nip, "Niepoprawny NIP", "Nip przeszedl a nie powinien")
    def test_nip_nie_liczba(self):
        nip="abc34"
        konto=KontoFirma(self.nazwa, nip,0)
        self.assertEqual(konto.nip, "Niepoprawny NIP", "Nip przeszedl a nie powinien")
    def test_Konto_express_srodki_sa(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, None)
        konto.saldo = 500
        konto.expressOutTransfer(100)
        self.assertEqual(konto.saldo, 399, "saldo po przelewie sie nie zgadza")
    def test_Konto_express_srodkow_brak(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, None)
        konto.expressOutTransfer(100)
        self.assertEqual(konto.saldo, 0, "saldo po przelewie sie nie zgadza")
    def test_Konto_express_srodkow_rowno(self):
        konto=Konto(self.name, self.nazwisko, self.pesel, "PROM_XYZ")
        konto.expressOutTransfer(50)
        self.assertEqual(konto.saldo, -1, "saldo po przelewie sie nie zgadza")
    def test_Firma__express_srodki_sa(self):
        konto=KontoFirma(self.nazwa, 1234567890, 100)
        konto.expressOutTransfer(50)
        self.assertEqual(konto.saldo, 45, "saldo po przelewie sie nie zgadza")
    def test_Firma__express_srodkow_brak(self):
        konto=KontoFirma(self.nazwa, 1234567890, 100)
        konto.expressOutTransfer(200)
        self.assertEqual(konto.saldo, 100, "saldo po przelewie sie nie zgadza")
    def test_Firma__express_srodki_rowno(self):
        konto=KontoFirma(self.nazwa, 1234567890, 100)
        konto.expressOutTransfer(100)
        self.assertEqual(konto.saldo, -5, "saldo po przelewie sie nie zgadza")







        