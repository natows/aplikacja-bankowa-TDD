# import unittest, requests, json

# class TestBackupRegistryApi(unittest.TestCase):
#     filepath = "app/registryBackup.json"
#     url = "http://127.0.0.1:5000/api/accounts"

#     body = {
#         "name": 'Dariusz',
#         "surname": "Januszewski",
#         "pesel": "04282301111"
#     }
#     body2 = {
#         "name": "Natalia",
#         "surname": "Owsiejko",
#         "pesel": "12345678910"
#     }

#     def setUp(self):
#         requests.post(self.url, json=self.body)
#         with open(self.filepath, "w", encoding="utf-8") as file:
#             json.dump([], file, indent=4)
#     def tearDown(self):
#         requests.delete(self.url + "/" + self.body["pesel"])


#     def test_saveBackupData(self):
#         response = requests.post(self.url + "/save")
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("Backup data saved successfully", response.json()["message"])

        

#     def test_loadBackupData(self):
#         with open(self.filepath, "w", encoding="utf-8") as file:
#             json.dump(self.body2, file, indent=4)
#         response = requests.post(self.url + "/load")
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("Backup data loaded successfully", response.json()["message"])



