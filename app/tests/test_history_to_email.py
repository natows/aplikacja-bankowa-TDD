import unittest

from unittest.mock import MagicMock
from unittest.mock import patch


from ..PersonalAccount import PersonalAccount
from ..FirmAccount import FirmAccount
from ..SMTPClient import SMTPClient


class TestSendHistoryToEmail(unittest.TestCase):
    email="nowsiejko@studms.pl"
    name = 'Ania'
    surname = 'Gotuje'
    pesel = '92012345678'
    firm_name="spolka sp. z.o.o"
    nip = 1234567890

    #personal account
    @patch('requests.get')
    def setUp(self, mock_get):
        self.smtp = SMTPClient()
        self.account = PersonalAccount(self.name, self.surname, self.pesel)

        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        self.firmAccount = FirmAccount(self.firm_name, self.nip)

    def test_send_succesfull_personal(self):
        self.smtp.send = MagicMock(return_value=True)
        self.account.history=[100,500,200]
        result = self.account.sendHistoryToEmail(self.email, self.smtp)
        self.assertTrue(result)

    def test_send_failed_personal(self):
        self.smtp.send = MagicMock(return_value=False)
        self.account.history=[100,500,200]
        result = self.account.sendHistoryToEmail(self.email, self.smtp)
        self.assertFalse(result)

    #firm account

    def test_send_succesful_firm(self):
        self.smtp.send = MagicMock(return_value=True)
        self.firmAccount.history=[100,200,430]
        result = self.firmAccount.sendHistoryToEmail(self.email, self.smtp)
        self.assertTrue(result)

    def test_send_failed_firm(self):
        self.smtp.send = MagicMock(return_value=False)
        self.firmAccount.history=[100,200,430]
        result = self.firmAccount.sendHistoryToEmail(self.email, self.smtp)
        self.assertFalse(result)
        



    
