class Konto:
    def __init__(self, imie, nazwisko, pesel, kod = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel = "Niepoprawny pesel"
        else:
            self.pesel = pesel
        if self.checkingPromotionCode(kod) and self.checkingAgebyPESEL(pesel):
            self.saldo = 50

    def checkingPromotionCode(self, code):
        return (code is not None and code[0:5] == "PROM_" and len(code)==8)
    def checkingAgebyPESEL(self,pesel):
        return  int(pesel[0:2]) > 60 or pesel[2]=="2" or pesel[2]=="3" #zakladajac ze nikt ponad setki nie dozyje