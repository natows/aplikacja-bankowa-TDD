import unittest, requests, json, os

class TestBackupRegistryApi(unittest.TestCase):
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
    body3 = {
        "name": "Zygmunt",
        "surname": "Waza",
        "pesel": "12345678911"
    }

    def setUp(self):
        requests.post(self.url, json=self.body)
        requests.post(self.url, json=self.body2)
        requests.post(self.url, json=self.body3)
        self.full_path = os.path.abspath("app/registry_backup.json")
        with open(self.full_path, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
        
    def tearDown(self):
        requests.delete(self.url + "/" + self.body["pesel"])
        requests.delete(self.url + "/" + self.body2["pesel"])
        requests.delete(self.url + "/" + self.body3["pesel"])

    def test_saveBackupData(self):
        response = requests.post(self.url + "/save", json={"filepath": self.full_path})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Backup data saved successfully", response.json()["message"])

    def test_loadBackupData(self):
        with open(self.full_path, "w", encoding="utf-8") as file:
            json.dump([self.body2, self.body3], file, indent=4)
        
        response = requests.post(self.url + "/load", json={"filepath": self.full_path})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Backup data loaded successfully", response.json()["message"])
        
        response = requests.get(self.url + "/count")
        self.assertEqual(response.json()["Count"], 2)

    def test_failedLoadingBackup(self):
        invalid_filepath = "zla/sciezka"
        response = requests.post(self.url + "/load", json={"filepath": invalid_filepath})
        self.assertEqual(response.status_code, 404)
