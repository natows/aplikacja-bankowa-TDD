from .AccountMain import Account

class FirmAccount(Account):
    def __init__(self, firm_name, nip):
        self.firm_name = firm_name
        if len(str(nip))!=10 or not str(nip).isdigit():
            self.nip = "Wrong NIP"
        else: self.nip = nip
        self.balance = 0
        self.history = []
    def outTransfer(self, amount):
        return super().outTransfer(amount)
    def inTransfer(self, amount):
        return super().inTransfer(amount)
    def expressOutTransfer(self, amount, fee=5):
        return super().expressOutTransfer(amount, fee)