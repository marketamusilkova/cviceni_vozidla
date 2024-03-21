# cvičení 5

# Svítí nám kontrolka_paliva, takže je potřeba tankovat.

# Přidej všem vozidlům (Auto, Autobus, Motorka) metodu natankuj, která má jeden parametr - počet litrů paliva.
# Metoda zařídí natankování paliva a zajistí, abychom nádrž nepřeplnili (pokud má nádrž 60 l a my chceme tankovat 100 l, natankuje se pouze maximum, které se do nádrže vejde).
# Metoda vrací počet natankovaných litrů.

# Otestujte (například) pomocí:

# auto2 = Auto('1B10000')
# print(auto2.natankuj(20), auto2.stav_nadrze)  # 20 20
# print(auto2.natankuj(20), auto2.stav_nadrze)  # 20 40
# print(auto2.natankuj(25), auto2.stav_nadrze)  # 10 50
# print(auto2.natankuj(25), auto2.stav_nadrze)  # 0 50

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
    
    def natankuj (self, natankované_litry_paliva):
        pridane_palivo = min(natankované_litry_paliva,self.velikost_nadrze - self.stav_nadrze)
        self.stav_nadrze += pridane_palivo
        return pridane_palivo
        
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

auto2 = Auto('1B10000')
print(auto2.natankuj(20), auto2.stav_nadrze)  
print(auto2.natankuj(20), auto2.stav_nadrze)  
print(auto2.natankuj(25), auto2.stav_nadrze)  
print(auto2.natankuj(25), auto2.stav_nadrze)  
