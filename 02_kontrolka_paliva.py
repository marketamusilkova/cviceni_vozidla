# cvičení 4

# Z výroby mají všechna vozidla prázdnou nádrž. Bohužel jsme při výrobě zapomněli přidat kontrolku paliva, která by nás na prázdnou či docházející nádrž upozornila.
# Přidej všem vozidlům (Auto, Autobus, Motorka) metodu kontrolka_paliva, která svítí (vrací True), pokud je stav paliva pod 10 % kapacity nádrže (v opačném případě vrací False).

class Vozidlo:
    def __init__(self, spz,):
        self.spz = spz
        self.spotreba = 10
        self.velikost_nadrze = 50
        self.stav_nadrze = 0

    def dojezd(self):
        return self.stav_nadrze / self.spotreba * 100
    
    def kontrolka_paliva(self):
       return self.stav_nadrze < 0.1 * self.velikost_nadrze

class Auto(Vozidlo):
    def __init__(self, spz):
        super().__init__(spz)

class Motorka(Vozidlo):
    def __init__(self, spz):
        super().__init__(spz)
        self.spotreba = 5
        self.velikost_nadrze = 15

class Autobus(Vozidlo):
    def __init__(self, spz):
        super().__init__(spz)
        self.spotreba = 25
        self.velikost_nadrze = 400

auto = Auto('1A10000')
print(auto.spz, auto.velikost_nadrze, auto.spotreba, auto.kontrolka_paliva())
   
moto = Motorka('2A10000')
print(moto.spz, moto.velikost_nadrze, moto.spotreba, moto.kontrolka_paliva())

bus = Autobus('3A10000')
print(bus.spz, bus.velikost_nadrze, bus.spotreba, bus.kontrolka_paliva())
