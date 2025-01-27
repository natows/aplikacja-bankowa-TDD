import unittest, requests
from ..AccountRegistry import AccountRegistry

class TestBackupRegistryApi():
    filepath = "app/registryBackup.json"
    url = "http://127.0.0.1:5000/api/accounts"

    body = {
        "name": 'Dariusz',
        "surname": "Januszewski",
        "pesel": "04282301111"
    }
    body2 = {
        "name": "Natalia",
        "surname": "Owsiejko",
        "pesel": "12345678910"
    }

    def setUp(self):
        self.registry = AccountRegistry
        response = requests.post(self.url, json=self.body)
        self.assertEqual(response.status_code, 201)

    def test_saveBackupData(self):
        return
    
    def test_loadBackupData(self):
        return
