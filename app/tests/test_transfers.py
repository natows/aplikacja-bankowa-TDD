import unittest

from ..PersonalAccount import PersonalAccount
from ..FirmAccount import FirmAccount

class Transfers(unittest.TestCase):
    name = 'Dariusz'
    nazwisko = "Januszewski"
    pesel = "042823011111"
    nazwa="spolka sp. z.o.o"
    nip = 1234567890
    
    def test_inTransfer(self):
        account=PersonalAccount(self.name, self.nazwisko, self.pesel, None)
        account.inTransfer(1500)
        self.assertEqual(account.balance, 1500, "Przelew nie przyszedl")
    def test_outTransfer_srodki_sa(self):
        account=PersonalAccount(self.name, self.nazwisko, self.pesel, None)
        account.balance=500
        account.outTransfer(200)
        self.assertEqual(account.balance, 300, "Przelew nie przeszedl")
    def test_outTransfer_srodkow_brak(self):
        account=PersonalAccount(self.name, self.nazwisko, self.pesel, None)
        account.outTransfer(200)
        self.assertEqual(account.balance, 0, "Przelew nie przeszedl")  
    def test_express_srodki_sa(self):
        account=PersonalAccount(self.name, self.nazwisko, self.pesel)
        account.balance = 500
        account.expressOutTransfer(100)
        self.assertEqual(account.balance, 399, "balance po przelewie sie nie zgadza")
    def test_express_srodkow_brak(self):
        account=PersonalAccount(self.name, self.nazwisko, self.pesel, None)
        account.expressOutTransfer(100)
        self.assertEqual(account.balance, 0, "balance po przelewie sie nie zgadza")
    def test_Konto_express_srodkow_rowno(self):
        account=PersonalAccount(self.name, self.nazwisko, self.pesel, "PROM_XYZ")
        account.expressOutTransfer(50)
        self.assertEqual(account.balance, -1, "balance po przelewie sie nie zgadza")

    #testy firmy
    def test_firma_przelew_przychodzacy(self):
        account=FirmAccount(self.nazwa, self.nip)
        account.inTransfer(100)
        self.assertEqual(account.balance, 100, "Saldo si enie zgadza")
    def test_firma_przelew_wychodzacy_udany(self):
        account=FirmAccount(self.nazwa, self.nip)
        account.balance=150
        account.outTransfer(100)
        self.assertEqual(account.balance, 50, "Saldo si enie zgadza")
    def test_firma_przelew_wychodzacy_nieudany(self):
        account=FirmAccount(self.nazwa, self.nip)
        account.outTransfer(100)
        self.assertEqual(account.balance, 0, "Saldo sie nie zgadza")
    def test_Firma__express_srodki_sa(self):
        account=FirmAccount(self.nazwa, self.nip)
        account.balance=100
        account.expressOutTransfer(50)
        self.assertEqual(account.balance, 45, "balance po przelewie sie nie zgadza")
    def test_Firma__express_srodkow_brak(self):
        account=FirmAccount(self.nazwa, self.nip)
        account.balance=100
        account.expressOutTransfer(200)
        self.assertEqual(account.balance, 100, "balance po przelewie sie nie zgadza")
    def test_Firma__express_srodki_rowno(self):
        account=FirmAccount(self.nazwa, self.nip)
        account.balance=100
        account.expressOutTransfer(100)
        self.assertEqual(account.balance, -5, "balance po przelewie sie nie zgadza")

    #test historii przelewow
    def test_konto(self):
        account=PersonalAccount(self.name,self.nazwisko,self.pesel)
        account.inTransfer(500)
        account.outTransfer(150)
        account.expressOutTransfer(250)
        self.assertEqual(account.history, [500,-150,-250,-1], "history sie nie zgadza")
    def test_konto_firmowe(self):
        account=FirmAccount(self.nazwa, self.nip)
        account.inTransfer(500)
        account.outTransfer(150)
        account.expressOutTransfer(250)
        self.assertEqual(account.history, [500,-150,-250,-5], "history sie nie zgadza")








        