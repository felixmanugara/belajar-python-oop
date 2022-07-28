
class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def getInfo(self):
        print("{} dengan health: {}".format(self.name, self.health))

"""
kita bisa mengunakan super() untuk menurunkan semua method yang ada pada 
super class di atas
"""        

class Mage(Hero):
    
    def __init__(self, name):
        super().__init__(name, 100)
        super().getInfo()
        
"""
atau kita juga bisa mengunakan nama dari super class itu sendiri, 
tetapi memiliki kelemahan yaitu jika nama super class diganti kita 
harus menggantinya juga pada class yang diwarsikan

"""

class Marksman(Hero):

    def __init__(self, name):
        Hero.__init__(self, name, 200)
        Hero.getInfo(self)
        


Kagura = Mage("Kagura")
Lesley = Marksman("Lesley")

