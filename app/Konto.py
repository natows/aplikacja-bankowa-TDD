class Konto:
    def __init__(self, imie, nazwisko, pesel, kod):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel = "Niepoprawny pesel"
        else:
            self.pesel = pesel
        if kod[0:4] == "PROM_" and len(kod)==8:
            self.saldo = 50
        else:
            self.saldo = 0