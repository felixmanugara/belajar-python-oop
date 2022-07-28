# latihan oop sederhana interaksi 2 objek
# yang saling menyerang

class Hero:
    
    def __init__(self, Name, Health, Attack, Defense, ItemCount):
        self.Name = Name
        self.Health = Health
        self.AttackPower = Attack
        self.Defense = Defense
        self.Item = ItemCount
        #print(self.__dict__)
    
    def attack(self, OpponentHero):
        # OpponentHero adalah objek lain dalam contoh ini Akaza
        print(self.Name + " Menyerang " + OpponentHero.Name)
        # self di sini merujuk pada 
        OpponentHero.attacked(self.Name,self.AttackPower)
        OpponentHero.getHealth()
    
    def attacked(self, Attacker, AttackerPower):

        print(self.Name + " diserang " + Attacker)
        AttackReceived = int(AttackerPower / self.Defense)
        print("Serangan Diterima: " + str(AttackReceived))
        self.Health -= AttackReceived
    
    def getHealth(self):
        print("Jumlah Health " + self.Name + " tersisa: " + str(self.Health))
    
    def healthUp(self, AddHealth):
        print(self.Name + " menggunakan Item untuk menambah Health, jumlah item saat ini " + str(self.Item))
        print("item digunakan: " + str(AddHealth))
        self.Item -= AddHealth
        AddedHealth = AddHealth * 10
        CurrentHealth = self.Health + AddedHealth
        print("Health diterima: ", AddedHealth)
        print("Health berhasil ditambahkan, jumlah Health " + self.Name + " saat ini: " + str(CurrentHealth))
        print(str(AddHealth) + " Item telah digunakan oleh " + self.Name + ", item tersisa: " + str(self.Item))
    
Rengoku = Hero("Rengoku Kyojuro", 100, 15, 10,5)
Akaza = Hero("Akaza", 100, 20, 6, 4)

Rengoku.attack(Akaza)
#Akaza.HealthUp(1)
#print('\n')
#Akaza.Attack(Rengoku)
#Rengoku.healthUp(2)

