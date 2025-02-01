import unittest

from ..PersonalAccount import PersonalAccount
from parameterized import parameterized

class TestTransfers(unittest.TestCase):
    name = 'Dariusz'
    surname = "Januszewski"
    pesel = "04282301111"

    def setUp(self):
        self.account=PersonalAccount(self.name,self.surname,self.pesel)
    

    def test_inTransfer(self):
        self.account.inTransfer(1500)
        self.assertEqual(self.account.balance, 1500, "The transfer failed")
    

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


    





        