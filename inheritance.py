class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

class Mage(Hero):
    pass

class Marskman(Hero):
    pass 

asal = Hero("asal",100)
Kagura = Mage("Kagura",100)
Lesley = Marskman("Lesley",100)

