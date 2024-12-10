import unittest
  
from unittest.mock import patch

from ..PersonalAccount import PersonalAccount
from ..FirmAccount import FirmAccount

from parameterized import parameterized

class TestCreateBankAccount(unittest.TestCase):
    name = 'Dariusz'
    surname = "Januszewski"
    pesel="12345678901"
    firm_name="spolka sp. z.o.o"
    nip = 1234567890

    @patch('requests.get')
    def setUp(self, mock_get):
        self.account=PersonalAccount(self.name,self.surname,self.pesel)

        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        self.firmAccount = FirmAccount(self.firm_name, self.nip)

    def test_makeAccount(self):
        self.assertEqual(self.account.name, self.name)
        self.assertEqual(self.account.surname, self.surname)
        self.assertEqual(self.account.balance, 0)
        self.assertEqual(self.account.pesel, self.pesel)


    def test_pesel_wrongLen(self):  #test dobrego peselu jest przy tworzneiu konta
        pesel = "123435674647632"
        account = PersonalAccount(self.name, self.surname, pesel)
        self.assertEqual(account.pesel, "Wrong PESEL", "Pesel nie zostal zapisany")
    

    @parameterized.expand([
        ("Age okay and Correct promotion code","12345678901", "PROM_123", 50),
        ("Age okay but Wrong prefix","12345678901", "Prom_123", 0),
        ("Age okay but Suffix too long", "12345678901", "PROM_1234",0),
        ("Code okay but age wrong", "44092929292", "PROM_XYZ", 0)

    ])
    def test_promCodewithAgeCheck(self, name, pesel, code, balance): 
        account=PersonalAccount(self.name, self.surname, pesel, code)
        self.assertEqual(account.balance, balance)
    
    

    # konta firmowe

    def test_makeFirmAccount(self):
        self.assertEqual(self.firmAccount.firm_name, self.firm_name)
        self.assertEqual(self.firmAccount.nip, self.nip)
        self.assertEqual(self.firmAccount.balance, 0)    

    @parameterized.expand([
        ("Wrong NIP length", 234, "Wrong NIP"), #test dobrego nipu jest przy tworzeniu konta
        ("NIP is not a number", "abc24", "Wrong NIP")
    ])
    def test_firmNip(self, name, nip, expected): 
        account=FirmAccount(self.firm_name, nip)
        self.assertEqual(account.nip, expected)

    @patch('app.FirmAccount.requests.get')
    def test_checkNip_valid(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = FirmAccount.checkNip("1234567890")

        self.assertTrue(result)


    @patch('app.FirmAccount.requests.get')
    def test_checkNip_wrong(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = FirmAccount.checkNip("1111111119")

        self.assertFalse(result)
        
        with self.assertRaises(ValueError) as context:
            FirmAccount(firm_name="Test Firm", nip="1111111119")  

        self.assertEqual(str(context.exception), "Company not registered!!")

    




    





        




        
    