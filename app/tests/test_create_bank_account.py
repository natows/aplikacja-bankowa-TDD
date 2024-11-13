import unittest

from ..PersonalAccount import PersonalAccount

from ..FirmAccount import FirmAccount

class TestCreateBankAccount(unittest.TestCase):
    name = 'Dariusz'
    surname = "Januszewski"
    pesel="12345678901"
    firm_name="spolka sp. z.o.o"
    nip = 1234567890

    def test_tworzenie_konta(self):
        account = PersonalAccount(self.name, self.surname, self.pesel)
        self.assertEqual(account.name, self.name, "name nie zostało zapisane!")
        self.assertEqual(account.surname, self.surname, "surname nie zostało zapisane!")
        self.assertEqual(account.balance, 0, "Saldo nie jest zerowe!")
        self.assertEqual(account.pesel, self.pesel, "Pesel nie został zapisany")


    def test_za_dlugi_pesel(self):
        pesel = "123435674647632"
        account = PersonalAccount(self.name, self.surname, pesel)
        self.assertEqual(account.pesel, "Wrong PESEL", "Pesel nie zostal zapisany")
    def test_zbyt_krotki_pesel(self):
        pesel = "1234"
        account = PersonalAccount(self.name, self.surname, pesel)
        self.assertEqual(account.pesel, "Wrong PESEL", "Pesel nie zostal zapisany")
    def test_kod_promocyjny_poprawny(self): 
        kod = "PROM_123"
        account=PersonalAccount(self.name, self.surname, self.pesel, kod)
        self.assertEqual(account.balance, 50, "Promocja nie zostala naliczona")
    def test_kod_promocyjny_zaDlugikoniec(self): 
        kod = "PROM_1234"
        account=PersonalAccount(self.name, self.surname, self.pesel, kod)
        self.assertEqual(account.balance, 0, "Promocja zostala naliczona po mimo złego kodu")
    def test_kod_promocyjny_zlyPoczatek(self): 
        kod = "PRom_123"
        account=PersonalAccount(self.name, self.surname, self.pesel, kod)
        self.assertEqual(account.balance, 0, "Promocja nie zostala naliczona")
    def test_wieku_dobry(self):
        pesel = "19292929292"
        kod = "PROM_124"
        account = PersonalAccount(self.name,self.surname,pesel,kod)
        self.assertEqual(account.balance, 50, "Promocja nie zostala naliczona")
    def test_wieku_zly(self):
        pesel = "44092929292"
        kod = "PROM_124"
        account = PersonalAccount(self.name,self.surname,pesel,kod)
        self.assertEqual(account.balance, 0, "Promocja nie zostala naliczona")


    # konta firmowe

    def test_tworzenie_konta_firmowego(self):
        account=FirmAccount(self.firm_name, self.nip)
        self.assertEqual(account.firm_name, self.firm_name, "Zła firm_name")
        self.assertEqual(account.nip, self.nip, "Zły nip")
        self.assertEqual(account.balance, 0, "Saldo nie jest zerowe")    

    def test_firma_nip_zla_dlugosc(self):
        nip=234
        account=FirmAccount(self.firm_name, nip)
        self.assertEqual(account.nip, "Wrong NIP", "Nip przeszedl a nie powinien")
    def test_nip_nie_liczba(self):
        nip="abc34"
        account=FirmAccount(self.firm_name, nip)
        self.assertEqual(account.nip, "Wrong NIP", "Nip przeszedl a nie powinien")
    





        




        
    