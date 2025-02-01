import unittest
  


from ..PersonalAccount import PersonalAccount


from parameterized import parameterized

class TestCreateBankAccount(unittest.TestCase):
    name = 'Dariusz'
    surname = "Januszewski"
    pesel="12345678901"


    def setUp(self):
        self.account=PersonalAccount(self.name,self.surname,self.pesel)


    def test_makeAccount(self):
        self.assertEqual(self.account.name, self.name)
        self.assertEqual(self.account.surname, self.surname)
        self.assertEqual(self.account.balance, 0)
        self.assertEqual(self.account.pesel, self.pesel)


    def test_pesel_wrongLen(self):  #test dobrego peselu jest przy tworzneiu konta
        pesel = "123435674647632"
        account = PersonalAccount(self.name, self.surname, pesel)
        self.assertEqual(account.pesel, "Wrong PESEL")
    

    @parameterized.expand([
        ("Age okay and Correct promotion code","12345678901", "PROM_123", 50),
        ("Age okay but Wrong prefix","12345678901", "Prom_123", 0),
        ("Age okay but Suffix too long", "12345678901", "PROM_1234",0),
        ("Code okay but age wrong", "44092929292", "PROM_XYZ", 0)

    ])
    def test_promCodewithAgeCheck(self, name, pesel, code, balance): 
        account=PersonalAccount(self.name, self.surname, pesel, code)
        self.assertEqual(account.balance, balance)
    
    

    




    





        




        
    