import unittest 

from unittest.mock import patch
from ..PersonalAccount import PersonalAccount
from ..FirmAccount import FirmAccount
from parameterized import parameterized

class TestLoans(unittest.TestCase):
    name = 'Dariusz'
    surname = "Januszewski"
    pesel = "04282301111"
    firm_name="spolka sp. z.o.o"
    nip = 1234567890

    @patch('requests.get')
    def setUp(self,mock_get):
        self.account=PersonalAccount(self.name,self.surname,self.pesel)

        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        self.firmAccount = FirmAccount(self.firm_name, self.nip)

    @parameterized.expand([
        ("Empty transfer history", [], 1000, 0),
        ("Three recent in-transfers", [-330, 1000, 2000,500], 2000, 2000),
        ("A recent negative transaction", [1000, -2000, 500], 2000, 0),
        ("The sum of 5 transfers greater that the loan", [1000, 2000, -500, 300, 100], 2000, 2000),
        ("The sum of 5 transfers lower that the loan", [1000, -2000, -500, -1000, 500], 2000, 0)

    ])
    def test_loanPersonal(self, name, history, loan, expected):
        self.account.history=history
        self.account.takeLoan(loan)
        self.assertEqual(self.account.balance, expected, "Balance is not right")
    
    @parameterized.expand([
        ("Self balance lower", 1000, 2000, [300, -1775, 100], 1000),
        ("No ZUS transfer", 1100, 500, [300, 1000,100], 1100),
        ("Balance higher and ZUS transfer", 2500, 1000, [200, -300, -1775, 400], 3500)

    ])
    def test_loanFirm(self, name, balance, loan, history, expected):
        self.firmAccount.balance = balance
        self.firmAccount.history = history
        self.firmAccount.takeLoan(loan)
        self.assertEqual(self.firmAccount.balance, expected)





    