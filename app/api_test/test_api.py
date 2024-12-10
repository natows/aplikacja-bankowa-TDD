import unittest, requests

from unittest.mock import patch


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
        response = requests.post(self.url, json = self.body)
        self.assertEqual(response.status_code, 201)

    def tearDown(self):
        response = requests.delete(self.url + "/" + self.body["pesel"])
        self.assertEqual(response.status_code, 200)
        
    

    def test_create_account(self):
        response = requests.post(self.url, json = self.body2)
        self.assertEqual(response.status_code, 201)




    

    def test_create_account_same_pesel(self):
        response = requests.post(self.url, json = self.body)
        self.assertEqual(response.status_code, 409)


    def test_count_accounts(self):
        response = requests.get(self.url + "/count")
        count = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count["Count"], 1)

    def test_check_peselOkay(self):
        response = requests.get(self.url + "/" + self.body['pesel'])
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
        response = requests.delete(self.url + "/"  + self.body2['pesel'])
        self.assertEqual(response.status_code, 200)
    
    def test_delete_nonexisting_acc(self):
        pesel = "123"
        response = requests.delete(self.url + "/"  + pesel)
        self.assertEqual(response.status_code, 404)

    def test_transfer_accNotFound(self):
        transfer ={
            "amount": 500,
            "type": "incoming"
        }
        response = requests.post(self.url + "/" + "00192929924" + "/transfer", json = transfer)
        self.assertEqual(response.status_code, 404)

    def test_inTransfer(self):
        transfer ={
            "amount": 500,
            "type": "incoming"
        }
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer)
        self.assertEqual(response.status_code, 200)


    def test_outTransfer_failed(self):
        transfer ={
            "amount": 600,
            "type": "outgoing"
        }
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer)
        self.assertEqual(response.status_code, 422)
    

    def test_outTransfer_succesful(self):
        transfer1 ={
            "amount": 250,
            "type": "incoming"
        }
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer1)
        self.assertEqual(response.status_code, 200)
        transfer2 ={
            "amount": 250,
            "type": "outgoing"
        }
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer2)
        self.assertEqual(response.status_code, 200)
    

    def test_expressOutTransfer_failed(self):
        transfer ={
            "amount": 600,
            "type": "express"
        }
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer)
        self.assertEqual(response.status_code, 422)


    def test_expressOutTransfer_succesful(self):
        transfer1 ={
            "amount": 250,
            "type": "incoming"
        }
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer1)
        self.assertEqual(response.status_code, 200)
        transfer2 ={
            "amount": 200,
            "type": "express"
        }
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer2)
        self.assertEqual(response.status_code, 200)



        

