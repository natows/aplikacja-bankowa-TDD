import unittest
from unittest.mock import patch

from ..PersonalAccount import PersonalAccount
from ..FirmAccount import FirmAccount

class TestTransferHistory(unittest.TestCase):
    name = 'Dariusz'
    surname = "Januszewski"
    pesel = "04282301111"
    firm_name="spolka sp. z.o.o"
    nip = 1234567890

    @patch('requests.get')
    def setUp(self, mock_get):
        self.account=PersonalAccount(self.name,self.surname,self.pesel)

        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        self.firmAccount = FirmAccount(self.firm_name, self.nip)

    def test_personalAccHistory(self):
        self.account.inTransfer(500)
        self.account.outTransfer(150)
        self.account.expressOutTransfer(250)
        self.assertEqual(self.account.history, [500,-150,-250,-1], "History is not right")

    def test_firmAccHistory(self):
        self.firmAccount.inTransfer(500)
        self.firmAccount.outTransfer(150)
        self.firmAccount.expressOutTransfer(250)
        self.assertEqual(self.firmAccount.history, [500,-150,-250,-5], "History is not right")