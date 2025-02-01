import unittest
from unittest.mock import patch
from ..FirmAccount import FirmAccount

from parameterized import parameterized

class TestCreateFirmAccount(unittest.TestCase):
    firm_name="spolka sp. z.o.o"
    nip = 1234567890


    @patch('requests.get')
    def setUp(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        self.firmAccount = FirmAccount(self.firm_name, self.nip)

    def test_makeFirmAccount(self):
        self.assertEqual(self.firmAccount.firm_name, self.firm_name)
        self.assertEqual(self.firmAccount.nip, self.nip)
        self.assertEqual(self.firmAccount.balance, 0)    

    @parameterized.expand([
        ("Wrong NIP length", 234, "Wrong NIP"), #test dobrego nipu jest przy tworzeniu konta
        ("NIP is not a number", "abc24", "Wrong NIP")
    ])
    def test_wrongNip(self, name, nip, expected): 
        account=FirmAccount(self.firm_name, nip)
        self.assertEqual(account.nip, expected)



    @patch('app.FirmAccount.requests.get')
    def test_checkNip_valid(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = FirmAccount.checkNip("1234512345")

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