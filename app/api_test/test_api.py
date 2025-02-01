import unittest, requests


class testAPICrud(unittest.TestCase):
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

    url = "http://127.0.0.1:5000/api/accounts"


    def setUp(self):
        requests.post(self.url, json = self.body)

    def tearDown(self):
        requests.delete(self.url + "/" + self.body["pesel"])
        requests.delete(self.url + "/" + self.body2["pesel"])
        
        
    

    def test_create_account(self):
        response = requests.post(self.url, json = self.body2)
        self.assertEqual(response.status_code, 201)
    

    def test_create_account_same_pesel(self):
        response = requests.post(self.url, json = self.body)
        self.assertEqual(response.status_code, 409)


    def test_count_accounts(self):
        initial_count = requests.get(self.url + "/count").json()["Count"]

        response = requests.post(self.url, json=self.body2)
        self.assertEqual(response.status_code, 201)

        new_count = requests.get(self.url + "/count").json()["Count"]
        self.assertEqual(new_count, initial_count + 1) 


    def test_get_acc_by_pesel_peselOkay(self):
        response = requests.get(self.url + "/" + self.body['pesel'])
        self.assertEqual(response.status_code, 200)
        account_data = response.json()
        self.assertEqual(account_data["name"], self.body["name"])
        self.assertEqual(account_data["surname"], self.body["surname"])
    
    def test_get_acc_by_pesel_peselWrong(self):
        pesel = "12345678901"
        response = requests.get(self.url + "/" + pesel)
        self.assertEqual(response.status_code, 404)

    def test_update_Acc(self):
        new = {"name": "Asia","surname": "Asiowa"}
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

    

