import unittest, requests

class PerformanceTests(unittest.TestCase):
    url = "http://127.0.0.1:5000/api/accounts"
    body = {
        "name": "Ola Aleksandra",
        "surname": "de Osrowska",
        "pesel": "10101010101"
    }
    transfer = {
        "amount": 100,
        "type": "incoming" 
    }

    iteration_count = 100
    timeout = 0.5

    def tearDown(self):
        requests.delete(self.url + f"/{self.body['pesel']}", timeout=self.timeout)

    def test_create_and_delete_100_accounts(self):
        for _ in range(self.iteration_count):
            response = requests.post(self.url, json = self.body, timeout=self.timeout)
            self.assertEqual(response.status_code, 201)
            response = requests.delete(self.url + f"/{self.body['pesel']}", timeout=self.timeout)
            self.assertEqual(response.status_code, 200)
        
    
    def test_create_acc_post_100_trasfers(self):
        response = requests.post(self.url, json=self.body)
        self.assertEqual(response.status_code, 201)
        for _ in range(self.iteration_count):
            response = requests.post(self.url + f"/{self.body['pesel']}/transfer", json = self.transfer, timeout=self.timeout)
            self.assertEqual(response.status_code, 200)
        expected_balance = self.transfer["amount"]*self.iteration_count
        account_data = response.json()
        real_balance = account_data["balance"]
        self.assertEqual(expected_balance, real_balance)


    
        
        



    