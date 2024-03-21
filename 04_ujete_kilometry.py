# cvičení 6

# [Bonus] Jsme skoro ready vyrazit. Schází 2 věci. Namontovat do vozidla počítadlo kilometrů (atribut najete_km) a metodu ujed.
# Metoda ujed dostane jako parametr kolik km má vozidlo ujet. Vozidlo ujede maximální počet km (s ohledem na dojezd). Metoda aktualizuje počítadlo km a stav nádrže a vrátí kolik km jsme v reálu ujeli.

# Otestujte (například) pomocí:

# auto3 = Auto('1C10000')
# print(auto3.natankuj(20), auto3.stav_nadrze, auto3.najete_km)  # 20 20 0
# print(auto3.ujed(100), auto3.stav_nadrze, auto3.najete_km)  # 100 10 100
# print(auto3.natankuj(20), auto3.stav_nadrze, auto3.najete_km)  # 20 30 100
# print(auto3.ujed(1000), auto3.stav_nadrze, auto3.najete_km)  # 300 0 400

class Vozidlo:
    def __init__(self, spz):
        self.spz = spz
        self.spotreba = 10
        self.velikost_nadrze = 50
        self.stav_nadrze = 0
        self.najete_km = 0

    def dojezd(self):
        return self.stav_nadrze / self.spotreba * 100
    
    def kontrolka_paliva(self):
       return self.stav_nadrze < 0.1 * self.velikost_nadrze
    
    def natankuj (self, natankované_litry_paliva):
        pridane_palivo = min(natankované_litry_paliva,self.velikost_nadrze - self.stav_nadrze)
        self.stav_nadrze += pridane_palivo
        return pridane_palivo
    
    def ujed(self, kolik_ma_ujet):
        ujete_km = min(kolik_ma_ujet, self.dojezd())
        self.najete_km += ujete_km
        self.stav_nadrze -= ujete_km / 100 * self.spotreba
        return ujete_km
       
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

auto3 = Auto('1C10000')
print(auto3.natankuj(20), auto3.stav_nadrze, auto3.najete_km)  
print(auto3.ujed(100), auto3.stav_nadrze, auto3.najete_km)  
print(auto3.natankuj(20), auto3.stav_nadrze, auto3.najete_km)  
print(auto3.ujed(1000), auto3.stav_nadrze, auto3.najete_km)  
