import unittest, requests

from app.AccountRegistry import AccountRegistry

from app.PersonalAccount import PersonalAccount

class testAPICrud(unittest.TestCase):
    body = {
        "name": 'Dariusz',
        "surname": "Januszewski",
        "pesel": "04282301111"
    }

    url = "http://127.0.0.1:5000/api/accounts"



    @classmethod
    def setUpClass(cls):
        cls.registry = AccountRegistry

    def test_create_account(self):
        response = requests.post(self.url, json = self.body)
        self.assertEqual(response.status_code, 201)

    def test_count_accounts(self):
        account = PersonalAccount("Natalia", "Nataliowa", "12345678900")
        self.registry.addAcc(account)
        response = requests.get(self.url + "/count")
        count = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count["Count"], 1)

    def test_check_peselOkay(self):
        requests.post(self.url, json = self.body)
        response = requests.get( self.url + "/" + self.body['pesel'])
        self.assertEqual(response.status_code, 201)
        account_data = response.json()
        self.assertEqual(account_data["name"], self.body["name"])
        self.assertEqual(account_data["surname"], self.body["surname"])
    
    def test_check_peselWrong(self):
        pesel = "12345678901"
        response = requests.get(self.url + "/" + pesel)
        self.assertEqual(response.status_code, 404)

    def test_update_Acc(self):
        new = {
            "name": "Asia",
            "surname": "Asiowa"
        }
        response = requests.patch(self.url + "/"  + self.body['pesel'], json = new)
        self.assertEqual(response.status_code, 200)
        account_data = response.json()
        self.assertEqual(account_data["name"], new["name"])
        self.assertEqual(account_data["surname"], new["surname"])
    
    def test_delete_existing_acc(self):
        response = requests.delete(self.url + "/"  + self.body['pesel'])
        self.assertEqual(response.status_code, 200)
    
    def test_delete_nonexisting_acc(self):
        pesel = "123"
        response = requests.delete(self.url + "/"  + pesel)
        self.assertEqual(response.status_code, 404)



