from .Konto import Konto

class KontoFirma(Konto):
    def __init__(self, nazwa, nip):
        self.nazwa = nazwa
        if len(str(nip))!=10 or not str(nip).isdigit():
            self.nip = "Niepoprawny NIP"
        else: self.nip = nip
        self.saldo = 0
        self.history = []
    def outTransfer(self, kwota):
        return super().outTransfer(kwota)
    def inTransfer(self, kwota):
        return super().inTransfer(kwota)
    def expressOutTransfer(self, kwota, oplata=5):
        return super().expressOutTransfer(kwota, oplata)