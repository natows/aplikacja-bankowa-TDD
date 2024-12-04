from .PersonalAccount import PersonalAccount

class AccountRegistry:
    accountList = []

    @classmethod
    def addAcc(cls, account):
        cls.accountList.append(account)
        
    @classmethod  
    def countAcc(cls):
        return len(cls.accountList)
    
    @classmethod
    def searchByPesel(cls, pesel):
        for i in cls.accountList:
            if i.pesel == pesel:
                return i
        return 
    
    @classmethod
    def updateAcc(cls, pesel, new):
        account = cls.searchByPesel(pesel)
        if account:
            account.name = new["name"] if "name" in new else account.name
            account.surname = new["surname"] if "surname" in new else account.surname
        return account

    @classmethod
    def removeAcc(cls, pesel):
        account = cls.searchByPesel(pesel)
        if account:
            cls.accountList.remove(account)
            return True
        return False
    

    
