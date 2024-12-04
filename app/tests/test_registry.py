import unittest


from ..AccountRegistry import AccountRegistry
from ..PersonalAccount import PersonalAccount


class Registry(unittest.TestCase):
    name1 = 'Dariusz'
    surname1 = "Januszewski"
    pesel1 = "04282301111"
    name2 = 'Ania'
    surname2 = 'Gotuje'
    pesel2 = '92012345678'

    @classmethod
    def setUpClass(cls):
        cls.registry = AccountRegistry
        cls.account1 = PersonalAccount(cls.name1, cls.surname1, cls.pesel1)
        cls.account2 = PersonalAccount(cls.name2, cls.surname2, cls.pesel2)
    
    def setUp(self):
        self.registry.addAcc(self.account1)
    
    def tearDown(self):
        self.registry.accountList = []


    def test_addAccount_and_countAccount(self):
        self.assertEqual(self.registry.countAcc(), 1)
    
    def test_findByPesel(self):
        found_acc = self.registry.searchByPesel(self.pesel1)
        self.assertEqual(found_acc, self.account1) 
        not_found_acc = self.registry.searchByPesel(self.pesel2)
        self.assertEqual(not_found_acc, None)
    
    def test_countAccounts(self):
        self.registry.addAcc(self.account2)
        self.assertEqual(self.registry.countAcc(), 2)

    def test_updateAcc(self):
        self.registry.updateAcc(self.pesel1,{"name": "Natalia", "surname": "Owsiejko"})
        account = self.registry.searchByPesel(self.pesel1)
        self.assertEqual(account.name, "Natalia")
        self.assertEqual(account.surname, "Owsiejko")

    def test_deleteAcc(self):
        self.registry.addAcc(self.account2)
        result = self.registry.removeAcc(self.pesel2)
        self.assertTrue(result)

    def test_delete_nonExistingAcc(self):
        result = self.registry.removeAcc("123")
        self.assertFalse(result)

    



    
        
