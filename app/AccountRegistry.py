from .PersonalAccount import PersonalAccount
import json

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
    

    @classmethod     
    def saveBackupData(cls, filename):
        data = []
        for account in cls.accountList:
            data.append({
                "name": account.name,
                "surname": account.surname,
                "pesel": account.pesel
            })
        with open(filename, "w", encoding = "utf-8") as file:
            json.dump(data, file, indent=4)

    @classmethod     
    def loadBackupData(cls, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        cls.accountList = []

        for acc_data in data:
            account = PersonalAccount(
                name=acc_data["name"],
                surname=acc_data["surname"],
                pesel=acc_data["pesel"]
            )
            cls.addAcc(account)

    

    
