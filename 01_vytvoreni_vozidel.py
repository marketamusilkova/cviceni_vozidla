# Pro následující úlohy můžete použít tuto základní třídu reprezentující vozidlo.

# class Vozidlo:
# def __init__(self, spz):
#     self.spz = spz
#     self.spotreba = 10
#     self.velikost_nadrze = 50
#     self.stav_nadrze = 0

# def dojezd(self):
#     '''
#     Vrátí dojezd vozidla v km.
#     '''
#     return self.stav_nadrze / self.spotreba * 100

# cvičení 1

# Vytvoř třídu Auto, která dědí z třídy Vozidlo. Auto má totožné parametry jako Vozidlo.

# Otestujte (například) pomocí:

# auto = Auto('1A10000')
# print(auto.spz, auto.velikost_nadrze, auto.spotreba) # 1A10000 50 10
class Vozidlo:
    def __init__(self, spz):
        self.spz = spz
        self.spotreba = 10
        self.velikost_nadrze = 50
        self.stav_nadrze = 0

    def dojezd(self):
        '''
        Vrátí dojezd vozidla v km.
        '''
        return self.stav_nadrze / self.spotreba * 100

class Auto(Vozidlo):
    pass

auto = Auto('1A10000')
print(auto.spz, auto.velikost_nadrze, auto.spotreba)

# cvičení 2

# Vytvoř třídu Motorka, která dědí z třídy Vozidlo. Motorka má spotřebu 5 (l na 100 km) a velikost nádrže 15 l.

# Otestujte (například) pomocí:

# moto = Motorka('2A10000')
# print(moto.spz, moto.velikost_nadrze, moto.spotreba) # 2A10000 15 5
class Vozidlo:
    def __init__(self, spz):
        self.spz = spz
        self.spotreba = 10
        self.velikost_nadrze = 50
        self.stav_nadrze = 0

    def dojezd(self):
        '''
        Vrátí dojezd vozidla v km.
        '''
        return self.stav_nadrze / self.spotreba * 100

class Motorka(Vozidlo):
    def __init__(self, spz):
        super().__init__(spz)
        self.spotreba = 5
        self.velikost_nadrze = 15

moto = Motorka('2A10000')
print(moto.spz, moto.velikost_nadrze, moto.spotreba)

# cvičení 3

# Vytvoř třídu Autobus, která dědí z třídy Vozidlo. Autobus má spotřebu 25 (l na 100 km) a velikost nádrže 400 l.

# Otestujte (například) pomocí:

# bus = Autobus('3A10000')
# print(bus.spz, bus.velikost_nadrze, bus.spotreba) # 3A10000 400 25
class Vozidlo:
    def __init__(self, spz):
        self.spz = spz
        self.spotreba = 10
        self.velikost_nadrze = 50
        self.stav_nadrze = 0

    def dojezd(self):
        '''
        Vrátí dojezd vozidla v km.
        '''
        return self.stav_nadrze / self.spotreba * 100

class Autobus(Vozidlo):
    def __init__(self, spz):
        super().__init__(spz)
        self.spotreba = 25
        self.velikost_nadrze = 400
    
bus = Autobus('3A10000')
print(bus.spz, bus.velikost_nadrze, bus.spotreba)
