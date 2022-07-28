class Hero1:
    Count = 0

    def __init__(self, Name, Attack, Health, Defense):
        self.name = Name
        self.attack = Attack
        self.health = Health
        self.defense = Defense

        # private variable
        self.__private = "ini adalah yang tidak bisa diakses dari luar class"

        # protected variable (sebaiknya tidak diubah-ubah)
        self._protected = "ini adalah variabel terproteksi"



testing = Hero1("Kamado",10,100,5)
print(testing.__dict__)
# bisa diakses karena name merupakan variabel public
print(testing.name)
# tidak bisa diakses dari luar class
print(testing.__private)
#print(testing.__dict__)
#print(testing._protected)
#testing._protected = "changes"
#print(testing._protected)
