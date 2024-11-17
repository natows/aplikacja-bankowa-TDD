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
    

