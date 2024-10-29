import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = 'Dariusz'
    nazwisko = "Januszewski"

    def test_tworzenie_konta(self):
        pesel = "12345678944"
        pierwsze_konto = Konto(self.imie, self.nazwisko, pesel, "x")
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, pesel, "pesel nie zostal zapisany")


    def test_zbyt_dlugi_pesel(self):
        pesel = "123435674647632"
        pierwsze_konto = Konto(self.imie, self.nazwisko, pesel, "PROM_123")
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel", "Pesel nie zostal zapisany")
    def test_zbyt_krotki_pesel(self):
        pesel = "1234"
        pierwsze_konto = Konto(self.imie, self.nazwisko, pesel, "PROM_123")
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel", "Pesel nie zostal zapisany")
    def test_kod_promocyjny_poprawny(self): 
        pesel =" 12345678901"
        kod = "PROM_123"
        pierwsze_konto=Konto(self.imie, self.nazwisko, pesel, kod)
        self.assertEqual(pierwsze_konto.saldo, 50, "Promocja nie zostala naliczona")
    def test_kod_promocyjny_zaDlugikoniec(self): 
        pesel =" 12345678901"
        kod = "PROM_1234"
        pierwsze_konto=Konto(self.imie, self.nazwisko, pesel, kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Promocja nie zostala naliczona")
    def test_kod_promocyjny_zlyPoczatek(self): 
        pesel =" 12345678901"
        kod = "PRom_123"
        pierwsze_konto=Konto(self.imie, self.nazwisko, pesel, kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Promocja nie zostala naliczona")
    def test_wieku_dobry(self):
        pesel = "33292929292"
        kod = "PROM_124"
        pierwsze_konto = Konto(self.imie,self.nazwisko,pesel,kod)
        self.assertEqual(pierwsze_konto.saldo, 50, "Promocja nie zostala naliczona")
    def test_wieku_zly(self):
        pesel = "44092929292"
        kod = "PROM_124"
        pierwsze_konto = Konto(self.imie,self.nazwisko,pesel,kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Promocja nie zostala naliczona")



        
    