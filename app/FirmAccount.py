import os, datetime, requests
from .AccountMain import Account

class FirmAccount(Account):
    def __init__(self, firm_name, nip):
        self.firm_name = firm_name
        if len(str(nip))!=10 or not str(nip).isdigit():
            self.nip = "Wrong NIP"
        elif self.checkNip(nip):
            self.nip = nip
        else:
            raise ValueError("Company not registered!!")   
        self.balance = 0
        self.history = []
    def outTransfer(self, amount):
        return super().outTransfer(amount)
    def inTransfer(self, amount):
        return super().inTransfer(amount)
    def expressOutTransfer(self, amount, fee=5):
        return super().expressOutTransfer(amount, fee)
    def takeLoan(self,amount):
        if self.balance >= 2*amount and -1775 in self.history:
            self.balance += amount

    @classmethod
    def checkNip(cls, nip):
        gov_url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        nip_path = f"{gov_url}api/search/nip/{nip}/?date={today}"
        print(f"Sending request to {nip_path}")
        response = requests.get(nip_path)
        print(f"Response for given nip: {response.status_code}, {response.json()}")
        if response.status_code == 200:
            return True
        return False
    
    def sendHistoryToEmail(self, email, smtp, text = "Historia konta Twojej firmy to:"):
        return super().sendHistoryToEmail(email, smtp, text)
  
