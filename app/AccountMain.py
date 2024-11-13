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
    def takeLoan(self,amount):  
        if self.check_3_last_transactions() or self.sum_of_5_last_trans(amount):
            self.balance += amount
    def check_3_last_transactions(self):
        return len(self.history) >= 3 and all(i > 0 for i in self.history[-3:]) 
    def sum_of_5_last_trans(self,amount):
        return len(self.history) >=5 and sum(self.history[-5:])>amount


