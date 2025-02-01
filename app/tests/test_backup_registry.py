import unittest, json

from ..AccountRegistry import AccountRegistry
from ..PersonalAccount import PersonalAccount

class TestBackupRegistry(unittest.TestCase):
    filepath = "app/registry_backup.json"
    person1 = {
        "name": "Zbych",
        "surname": "Zbyszkowy", 
        "pesel": "12345678910"
    }
    person2 = {
        "name": "Sigma", 
        "surname": "Boy", 
        "pesel": "10987654321"
    }
    person3 = {
        "name": "Jozef", 
        "surname": "K", 
        "pesel": "11111111111"     
    }

    def setUp(self):
        self.registry = AccountRegistry
        account1 = PersonalAccount(self.person1["name"], self.person1["surname"], self.person1["pesel"])
        account2 = PersonalAccount(self.person2["name"], self.person2["surname"], self.person2["pesel"])
        self.registry.accountList=[account1,account2]
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
        

    def tearDown(self):
        self.registry.accountList = []


    def test_saveBackupData(self):
        self.registry.saveBackupData(self.filepath)

        with open(self.filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        expected_data = [
            self.person1, 
            self.person2
        ]

        self.assertEqual(expected_data, data)

    def test_loadBackupData(self): 
        backup_data = [
            self.person2,
            self.person3
        ]
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(backup_data, file, indent=4)

        self.registry.loadBackupData(self.filepath)

        self.assertEqual(len(self.registry.accountList), 2)

        self.assertEqual(self.registry.accountList[0].name, self.person2["name"])
        self.assertEqual(self.registry.accountList[0].surname, self.person2["surname"])
        self.assertEqual(self.registry.accountList[0].pesel, self.person2["pesel"])

        self.assertEqual(self.registry.accountList[1].name, self.person3["name"])
        self.assertEqual(self.registry.accountList[1].surname, self.person3["surname"])
        self.assertEqual(self.registry.accountList[1].pesel, self.person3["pesel"])


    def test_loadBackupData_clearsRegistry(self):
        self.assertEqual(len(self.registry.accountList), 2)

        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

        self.registry.loadBackupData(self.filepath)

        self.assertEqual(len(self.registry.accountList), 0)