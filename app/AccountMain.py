class Account:
    def outTransfer(self,amount):
        if self.balance-amount >= 0 :
            self.balance -= amount
            self.history.append(-amount)
    def inTransfer(self,amount):
        self.balance += amount
        self.history.append(amount)
    def expressOutTransfer(self, amount, fee):
        if self.balance - amount >=0 :
            self.balance -= (amount + fee)
            self.history.append(-amount)
            self.history.append(-fee)
    


