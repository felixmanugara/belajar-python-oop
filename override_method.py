class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} health: {}".format(self.name,self.health))

    
class Mage(Hero):
    def __init__(self,name):
        super().__init__(name,100)
    
    #override method
    def showInfo(self):
        print("{}\ntipe: Mage\nhealth: {}".format(self.name,self.health))

class Marksman(Hero):
    def __init__(self,name):
        super().__init__(name,200)

Kagura = Mage("Kagura")
Lesley = Marksman("Lesley")

Kagura.showInfo()
Lesley.showInfo()

