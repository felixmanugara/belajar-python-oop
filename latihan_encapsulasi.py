class Hero:
    # private class variable
    __Count = 0

    def __init__(self,name,health,attackPower,defense,item):
        self.__name = name
        self.__baseHealth = health
        self.__baseAttPower = attackPower
        self.__baseDefense = defense
        self.__item = item

        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__baseHealth * self.__level
        self.__attPower = self.__baseAttPower * self.__level
        self.__defense = self.__baseDefense * self.__level

        self.__health = self.__healthMax

        Hero.__Count += 1
    
    @property
    def info(self):
        return "{} Level {}:\n\thealth: {}/{}\n\tattack power: {}\n\tdefense: {}\n\titem: {}\n".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__defense,self.__item)
    
    @property
    def gainHealth(self):
        pass
        
    @gainHealth.setter
    def gainHealth(self,addHealth):
        if (addHealth > self.__item):
            raise Exception("insufficient item, you have " + str(self.__item) + " item")
        else:
            self.__health += (addHealth * 10)
            self.__item -= addHealth
            print("Health added " + self.__name + " item left: " + str(self.__item) + "\n")

    @property
    def gainExp(self):
        pass
        #return self.__exp
    
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, "Level Up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__baseHealth * self.__level
            self.__attPower = self.__baseAttPower * self.__level
            self.__defense = self.__baseDefense * self.__level


    def attack(self,opponent):
        print(self.__name +" Menyerang " + opponent.__name + "\n")
        self.gainExp = 50
        opponent.__health -= (self.__attPower - opponent.__defense)


    

Akaza = Hero("Akaza",100,30,15,4)
Kamado = Hero("Kamado Tanjirou",100,20,12,3)
#print(Akaza.info)
#Akaza.gainExp = 100
#Akaza.gainExp = 150
#print(Akaza.info)
#print(Akaza.gainExp)
#Akaza.gainHealth = 1
print(Akaza.info)
print(Kamado.info)
#print(Kamado.info)
Akaza.attack(Kamado)
Kamado.attack(Akaza)
#Akaza.attack(Kamado)
#print(Akaza.info)
#Kamado.attack(Akaza)
#Kamado.attack(Akaza)
Kamado.gainHealth = 2
print(Kamado.info)
print(Akaza.info)