import unittest

from unittest.mock import MagicMock
from unittest.mock import patch
import datetime


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
    def setUp(self):
        self.smtp = SMTPClient()

        self.account = PersonalAccount(self.name, self.surname, self.pesel)
        self.account.history = [100, 500, 200]

        self.mock_get = patch('requests.get').start()
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        self.mock_get.return_value = mock_response
        self.firmAccount = FirmAccount(self.firm_name, self.nip)
        self.firmAccount.history = [100, 200, 300]

    def test_send_succesfull_personal(self):
        self.smtp.send = MagicMock(return_value=True)
        result = self.account.sendHistoryToEmail(self.email, self.smtp)
        self.assertTrue(result)
        self.smtp.send.assert_called_with(
            f"Wyciąg z dnia {datetime.datetime.today().strftime('%Y-%m-%d')}", 
            "Twoja historia konta to:" + str(self.account.history), self.email
        )

    def test_send_failed_personal(self):
        self.smtp.send = MagicMock(return_value=False)
        result = self.account.sendHistoryToEmail(self.email, self.smtp)
        self.assertFalse(result)
        self.smtp.send.assert_called_with(
            f"Wyciąg z dnia {datetime.datetime.today().strftime('%Y-%m-%d')}", 
            "Twoja historia konta to:" + str(self.account.history), 
            self.email
        )

    #firm account

    def test_send_succesful_firm(self):
        self.smtp.send = MagicMock(return_value=True)
        result = self.firmAccount.sendHistoryToEmail(self.email, self.smtp)
        self.assertTrue(result)
        self.smtp.send.assert_called_with(
            f"Wyciąg z dnia {datetime.datetime.today().strftime('%Y-%m-%d')}", 
            "Historia konta Twojej firmy to:" + str(self.firmAccount.history), 
            self.email
        )

    def test_send_failed_firm(self):
        self.smtp.send = MagicMock(return_value=False)
        result = self.firmAccount.sendHistoryToEmail(self.email, self.smtp)
        self.assertFalse(result)
        self.smtp.send.assert_called_with(
            f"Wyciąg z dnia {datetime.datetime.today().strftime('%Y-%m-%d')}", 
            "Historia konta Twojej firmy to:" + str(self.firmAccount.history), 
            self.email
        )
        



    
