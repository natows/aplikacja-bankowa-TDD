import unittest

from ..Konto import Konto


class Kredyty(unittest.TestCase):
    name = 'Dariusz'
    surname = "Januszewski"
    pesel = "042823011111"



    def test_empty_history(self):
        konto=Konto(self.name,self.surname, self.pesel)
        konto.takeLoan(1000)
        self.assertEqual(konto.saldo, 0, "Saldo się nie zgadza")
    
    def test_3_positive_transactions(self):
        konto=Konto(self.name,self.surname, self.pesel)
        konto.history=[-330, 1000, 2000, 500]
        konto.takeLoan(2000)
        self.assertEqual(konto.saldo, 2000, "Saldo się nie zgadza")
    def test_a_negative_transaction(self):
        konto=Konto(self.name,self.surname, self.pesel)
        konto.history=[1000, -2000, 500]
        konto.takeLoan(2000)
        self.assertEqual(konto.saldo, 0, "Saldo się nie zgadza")


    def test_sum_greater(self):
        konto=Konto(self.name,self.surname, self.pesel)
        konto.history=[1000, 2000, -500, 300, 100]
        konto.takeLoan(2000)
        self.assertEqual(konto.saldo, 2000, "Balance is not right")
    def test_sum_lower(self):
        konto=Konto(self.name,self.surname, self.pesel)
        konto.history=[1000, -2000, -500, -1000, 500]
        konto.takeLoan(2000)
        self.assertEqual(konto.saldo, 0, "Balance is not right")





    