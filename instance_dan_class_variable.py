class Hero:
    # class variable
    Count = 0 # class variabel

    def __init__(self,InputName,InputHealth,InputPower,InputDefense):
         # instance variabel
         self.Name = InputName 
         self.Health = InputHealth
         self.Power = InputPower
         self.Defense = InputDefense
         
         Hero.Count += 1 # count akan bertambah setiap objek dibuat
         print(self.Name, "berhasil ditambahkan, jumlah Hero saat ini", Hero.Count)

#HERO1 = Hero("Rengoku Kyojuro",100,15,20) 
#HERO2 = Hero("Akaza",100,18,10)
#HERO3 = Hero("Kamado Tanjirou",100,10,8)

#print(HERO1.__dict__)
#print(HERO2.Health)
#print(HERO3.Defense)
#print(Hero.Count)



