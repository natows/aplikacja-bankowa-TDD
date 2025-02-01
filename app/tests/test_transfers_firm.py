import unittest

from unittest.mock import patch
from ..FirmAccount import FirmAccount
from parameterized import parameterized

class TestFirmTransfers(unittest.TestCase):
    firm_name="spolka sp. z.o.o"
    nip = 1234567890

    @patch('requests.get')
    def setUp(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        self.firmAccount = FirmAccount(self.firm_name, self.nip)

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
