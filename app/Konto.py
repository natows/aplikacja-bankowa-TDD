class Konto:
    def __init__(self, name, surname, pesel, kod = None):
        self.name = name
        self.surname = surname
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel = "Niepoprawny pesel"
        else:
            self.pesel = pesel
        if self.checkingPromotionCode(kod) and self.checkingAgebyPESEL(pesel):
            self.saldo = 50     
        self.history = []  
            

    def checkingPromotionCode(self, code):
        return (code is not None and code[0:5] == "PROM_" and len(code)==8)
    def checkingAgebyPESEL(self,pesel):
        return  int(pesel[0:2]) > 60 or pesel[2]=="2" or pesel[2]=="3" 
    def outTransfer(self,kwota):
        if self.saldo-kwota >= 0 :
            self.saldo -= kwota
            self.history.append(-kwota)
    def inTransfer(self,kwota):
        self.saldo += kwota
        self.history.append(kwota)
    def expressOutTransfer(self, amount, oplata=1):
        if self.saldo - amount >=0 :
            self.saldo -= (amount + oplata)
            self.history.append(-amount)
            self.history.append(-oplata)
    def takeLoan(self,amount):  
        if self.check_3_last_transactions() or self.sum_of_5_last_trans(amount):
            self.saldo += amount
    def check_3_last_transactions(self):
        return len(self.history) >= 3 and all(i > 0 for i in self.history[-3:]) 
    def sum_of_5_last_trans(self,amount):
        return (len(self.history) >=5 and sum(self.history[-5:])>amount)


