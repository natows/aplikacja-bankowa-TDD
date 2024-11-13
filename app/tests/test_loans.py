import unittest

from ..PersonalAccount import PersonalAccount
from parameterized import parameterized

class Loans(unittest.TestCase):
    name = 'Dariusz'
    surname = "Januszewski"
    pesel = "042823011111"

    def setUp(self):
        self.account=PersonalAccount(self.name,self.surname,self.pesel)

    @parameterized.expand([
        ("Empty transfer history", [], 1000, 0),
        ("Three recent in-transfers", [-330, 1000, 2000, 500], 2000, 2000),
        ("A recent negative transaction", [1000, -2000, 500], 2000, 0),
        ("The sum of 5 transfers greater that the loan", [1000, 2000, -500, 300, 100], 2000, 2000),
        ("The sum of 5 transfers lower that the loan", [1000, -2000, -500, -1000, 500], 2000, 0)

    ])
    def test_loan(self, name, history, loan, expected):
        self.account.history=history
        self.account.takeLoan(loan)
        self.assertEqual(self.account.balance, expected, "Balance is not right"),

    # def test_empty_history(self):
    #     self.account.takeLoan(1000)
    #     self.assertEqual(self.account.balance, 0, "Balance is not correct")

    # def test_3_positive_transactions(self):
    #     self.account.history=[-330, 1000, 2000, 500]
    #     self.account.takeLoan(2000)
    #     self.assertEqual(self.account.balance, 2000, "Balance is not correct")
    # def test_a_negative_transaction(self):
    #     self.account.history=[1000, -2000, 500]
    #     self.account.takeLoan(2000)
    #     self.assertEqual(self.account.balance, 0, "Balance is not correct")

    # def test_sum_5_greater(self):
    #     self.account.history=[1000, 2000, -500, 300, 100]
    #     self.account.takeLoan(2000)
    #     self.assertEqual(self.account.balance, 2000, "Balance is not correct")

    # def test_sum_5_lower(self):
    #     self.account.history=[1000, -2000, -500, -1000, 500]
    #     self.account.takeLoan(2000)
    #     self.assertEqual(self.account.balance, 0, "Balance is not correct")





    