import unittest, requests

class TestApiTransfers(unittest.TestCase):
    url = "http://127.0.0.1:5000/api/accounts"
    
    body = {
        "name": 'Monika',
        "surname": "Kociołek",
        "pesel": "04282301155"
    }

    def setUp(self):
        requests.post(self.url, json = self.body)

    def tearDown(self):
        requests.delete(self.url + "/" + self.body["pesel"])

    def test_transfer_accNotFound(self):
        transfer ={ "amount": 500, "type": "incoming" }
        response = requests.post(self.url + "/0019/transfer", json = transfer)
        self.assertEqual(response.status_code, 404)

    def test_inTransfer(self):
        transfer ={ "amount": 500, "type": "incoming"}
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["balance"], 500)


    def test_outTransfer_failed(self):
        transfer ={"amount": 1000,"type": "outgoing"}
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer)
        self.assertEqual(response.status_code, 422)
    

    def test_outTransfer_succesful(self):
        transfer1 ={"amount": 500,"type": "incoming"}
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer1)
        self.assertEqual(response.status_code, 200)
        transfer2 ={"amount": 250,"type": "outgoing"}
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["balance"], 250)
    

    def test_expressOutTransfer_failed(self):
        transfer ={"amount": 600,"type": "express"}
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer)
        self.assertEqual(response.status_code, 422)


    def test_expressOutTransfer_succesful(self):
        transfer1 ={"amount": 250,"type": "incoming"}
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer1)
        self.assertEqual(response.status_code, 200)
        transfer2 ={"amount": 200,"type": "express"}
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["balance"], 49)

    def test_wrongTransferType(self):
        transfer ={"amount": 100,"type": "wrong"}
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer)
        self.assertEqual(response.status_code, 400)

    def test_wrongDataGiven(self):
        transfer ={"type": "incoming"}
        response = requests.post(self.url + "/" + self.body["pesel"] + "/transfer", json = transfer)
        self.assertEqual(response.status_code, 400)



        