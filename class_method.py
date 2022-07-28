# method adalah fungsi yang mengatur interaksi
# dan behavior dari sebuah objek / instance

class Hero:
    # class variable
    Count = 0 

    def __init__(self, InputName, InputHealth, InputPower, InputDefense):
        # instance / object variable (attribute)
        self.Name = InputName
        self.Health = InputHealth
        self.Power = InputPower
        self.Defense = InputDefense

        Hero.Count += 1

    # void function, (without parameter)
    def identify(self):
        print("Hero ini bernama "+ self.Name)
    # function with parameter
    def healthUp(self,AddHealth):
        self.Health += AddHealth
    
    # function with return value
    def getHealth(self):
        return self.Name + " Health " + str(self.Health)

HERO1 = Hero("Rengoku Kyojuro",100,15,20) 
HERO2 = Hero("Akaza",100,18,10)
HERO3 = Hero("Kamado Tanjirou",100,10,8)

HERO1.identify()
# menambahkan health value
HERO1.healthUp(5)
print(HERO1.getHealth())



    
