from .AccountMain import Account

class PersonalAccount(Account):
    def __init__(self, name, surname, pesel, kod = None):
        self.name = name
        self.surname = surname
        self.balance = 0
        if len(pesel) != 11:
            self.pesel = "Wrong PESEL"
        else:
            self.pesel = pesel

        if self.checkingPromotionCode(kod) and self.checkingAgebyPESEL(pesel):
            self.balance = 50     
        self.history = []  

    def checkingPromotionCode(self, code):
        return code is not None and code[0:5] == "PROM_" and len(code)==8
    def checkingAgebyPESEL(self,pesel):
        return  int(pesel[0:2]) > 60 or pesel[2]=="2" or pesel[2]=="3"
    def outTransfer(self, amount):
        return super().outTransfer(amount)
    def inTransfer(self, amount):
        return super().inTransfer(amount)
    def expressOutTransfer(self, amount, fee=1):
        return super().expressOutTransfer(amount, fee)
    def takeLoan(self, amount):
        return super().takeLoan(amount)
    