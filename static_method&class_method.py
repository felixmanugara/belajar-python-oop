class Hero:
    __Count = 0

    def __init__(self, Name):
        self.name = Name
        Hero.__Count += 1
    
    # method yang hanya berlaku untuk objek
    def getCount(self):
        return Hero.__Count
    
    # method yang hanya berlaku untuk class
    def getCount1():
        return Hero.__Count
    
    # static method berlaku untuk class dan objek
    @staticmethod # decorator untuk static method
    def getCount2():
        return Hero.__Count
    
    """
    static method memiliki kelemahan, yaitu jika nama class diganti kita
    harus mengganti juga nama class yang digunakan untuk memanggil variable
    di dalam method
    
    """
    
    # class method adalah method yang berlaku untuk class dan objek
    @classmethod # decorator untuk class method
    def getCount3(cls):
        return cls.__Count
    
    """
    kenapa butuh class method?
    dengan menggunakan class method kita akan dimudahkan dalam penggunaan atribut
    atau variable, karena jika nama class diganti kita tidak perlu repot2 mengganti 
    nama class yang digunakan dalam pemanggilan class variable, karena pada class 
    method kita telah menggunakan parameter cls sebagai wujud dari nama class.
    
    """


Akaza = Hero("Akaza")
# mengakses method dengan instance / objek
print(Akaza.getCount()) 
# mengakses method dengan class
print(Hero.getCount()) # will raise error
# mengakses method dengan instance / objek
print(Akaza.getCount1()) # will raise error
# mengakses method dengan class
print(Hero.getCount1())
# static method 
print(Hero.getCount2())
print(Akaza.getCount2())
# class method
print(Hero.getCount3())
print(Akaza.getCount3())