import unittest


from ..Konto import Konto

from ..konto_firmowe import KontoFirma

class TestCreateBankAccount(unittest.TestCase):
    imie = 'Dariusz'
    nazwisko = "Januszewski"
    pesel="12345678901"
    nazwa="spolka sp. z.o.o"
    nip = 1234567890

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany")


    def test_za_dlugi_pesel(self):
        pesel = "123435674647632"
        pierwsze_konto = Konto(self.imie, self.nazwisko, pesel)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel", "Pesel nie zostal zapisany")
    def test_zbyt_krotki_pesel(self):
        pesel = "1234"
        pierwsze_konto = Konto(self.imie, self.nazwisko, pesel)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel", "Pesel nie zostal zapisany")
    def test_kod_promocyjny_poprawny(self): 
        kod = "PROM_123"
        pierwsze_konto=Konto(self.imie, self.nazwisko, self.pesel, kod)
        self.assertEqual(pierwsze_konto.saldo, 50, "Promocja nie zostala naliczona")
    def test_kod_promocyjny_zaDlugikoniec(self): 
        kod = "PROM_1234"
        pierwsze_konto=Konto(self.imie, self.nazwisko, self.pesel, kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Promocja zostala naliczona po mimo złego kodu")
    def test_kod_promocyjny_zlyPoczatek(self): 
        kod = "PRom_123"
        pierwsze_konto=Konto(self.imie, self.nazwisko, self.pesel, kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Promocja nie zostala naliczona")
    def test_wieku_dobry(self):
        pesel = "19292929292"
        kod = "PROM_124"
        pierwsze_konto = Konto(self.imie,self.nazwisko,pesel,kod)
        self.assertEqual(pierwsze_konto.saldo, 50, "Promocja nie zostala naliczona")
    def test_wieku_zly(self):
        pesel = "44092929292"
        kod = "PROM_124"
        pierwsze_konto = Konto(self.imie,self.nazwisko,pesel,kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Promocja nie zostala naliczona")


    # konta firmowe

    def test_tworzenie_konta_firmowego(self):
        konto=KontoFirma(self.nazwa, self.nip)
        self.assertEqual(konto.nazwa, self.nazwa, "Zła nazwa")
        self.assertEqual(konto.nip, self.nip, "Zły nip")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")    

    def test_firma_nip_zla_dlugosc(self):
        nip=234
        konto=KontoFirma(self.nazwa, nip)
        self.assertEqual(konto.nip, "Niepoprawny NIP", "Nip przeszedl a nie powinien")
    def test_nip_nie_liczba(self):
        nip="abc34"
        konto=KontoFirma(self.nazwa, nip)
        self.assertEqual(konto.nip, "Niepoprawny NIP", "Nip przeszedl a nie powinien")
    





        




        
    