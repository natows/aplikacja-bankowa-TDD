import unittest

from unittest.mock import patch

from ..PersonalAccount import PersonalAccount
from ..FirmAccount import FirmAccount
from parameterized import parameterized

class Transfers(unittest.TestCase):
    name = 'Dariusz'
    surname = "Januszewski"
    pesel = "04282301111"
    firm_name="spolka sp. z.o.o"
    nip = 1234567890

    @patch('requests.get')
    def setUp(self, mock_get):
        self.account=PersonalAccount(self.name,self.surname,self.pesel)
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        self.firmAccount = FirmAccount(self.firm_name, self.nip)
    

    # TESTS FOR PERSONAL ACCOUNT

    def test_inTransfer(self):
        self.account.inTransfer(1500)
        self.assertEqual(self.account.balance, 1500, "Przelew nie przyszedl")
    

    @parameterized.expand([
        ("Enough funds for out-transfer", 500, 200, 300),
        ("Not enough funds for out-transfer", 0, 200, 0)
    ])
    def test_outTransfer(self, name, balance, amount, expected):
        self.account.balance=balance
        self.account.outTransfer(amount)
        self.assertEqual(self.account.balance, expected, "Balance is not right")


    @parameterized.expand([
        ("Enough funds for express-out-transfer", 500, 100, 399),
        ("Not enough funds for express-out-transfer", 0, 100, 0)
    ])
    def test_expressOutTransfer(self, name, balance, amount, expected):
        self.account.balance = balance
        self.account.expressOutTransfer(amount)
        self.assertEqual(self.account.balance, expected, "Balance is not right")


    #TESTS FOR FIRM ACCOUNT

    def test_firm_inTransfer(self):
        self.firmAccount.inTransfer(100)
        self.assertEqual(self.firmAccount.balance, 100, "Balance is not right")


    @parameterized.expand([
        ("Enough funds for out-transfer", 150, 100, 50),
        ("Not enough funds for out-transfer", 0, 200, 0)
    ])
    def test_firm_outTransfer(self, name, balance, amount, expected):
        self.firmAccount.balance=balance
        self.firmAccount.outTransfer(amount)
        self.assertEqual(self.firmAccount.balance, expected, "Balance is not right")



    @parameterized.expand([
        ("Enough funds for express-out-transfer", 500, 100, 395),
        ("Not enough funds for express-out-transfer", 20, 100, 20)
    ])
    def test_firm_expressOutTransfer(self, name, balance, amount, expected):
        self.firmAccount.balance = balance
        self.firmAccount.expressOutTransfer(amount)
        self.assertEqual(self.firmAccount.balance, expected, "Balance is not right")

    

    #TESTS FOR TRANSFER HISTORY

    def test_personalAccHistory(self):
        self.account.inTransfer(500)
        self.account.outTransfer(150)
        self.account.expressOutTransfer(250)
        self.assertEqual(self.account.history, [500,-150,-250,-1], "History is not right")
    def test_firmAccHistory(self):
        self.firmAccount.inTransfer(500)
        self.firmAccount.outTransfer(150)
        self.firmAccount.expressOutTransfer(250)
        self.assertEqual(self.firmAccount.history, [500,-150,-250,-5], "History is not right")





        