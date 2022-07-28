class Hero:

    def __init__(self, Name, Health, Defense):
        self.__name = Name
        self.__health = Health
        self.__defense = Defense
        #self.__info = "Name: {} \nDefense: {}".format(self.name,self.__defense)
    
    """
     membuat getter menggunakan method memiliki kelemahan jika atribut 
     dari sebuah objek diubah nilainya, getinfo tidak akan ikut berubah
     dan akan tetap nilainya, sehingga kita juga harus mengubah baris 
     code lain yang mempunyai akses ke atribut tersebut

    """
    def getInfo(self):
        return "Name: {} \nDefense: {}".format(self.__name,self.__defense)
    
    def defense(self):
        return self.__defense
    
    def adddefense(self, inputNum ):
        self.__defense += inputNum
    
Kamado = Hero("Kamado Tanjirou", 100, 50)    
#print(Kamado.getInfo())
#Kamado.name = "Akaza"
#print(Kamado.getInfo())
#print(Kamado.defense())
#Kamado.adddefense(5)
#print(Kamado.defense())
#print(Kamado.getInfo())

class Hero1:

    def __init__(self, Name, Health, Defense):
        self.__name = Name
        self.__health = Health
        self.__defense = Defense
 
    """
    dengan menggunakan decorator @property method akan dianggap sebagai sebuah
    variable dynamic, ini akan membuat getinfo ikut berubah nilainya jika atribut 
    dari sebuah instance diubah nilainya. Penggunaan decorator property juga dinilai
    baik untuk menekankankan bahwa atribut tertentu tidak dapat diubah sembarangan 
    dari luar class
    """
    @property
    def getInfo(self):
        return "Name: {} \nDefense: {}".format(self.__name,self.__defense)
    
    #@defense.getter
    #def defense(self):
        #return self.__defense
    
    # membuat getter dengan decorator @property
    @property
    def defense(self):
        return self.__defense
    
    # membuat setter
    @defense.setter
    def defense(self,InputNum):
        # logic untuk memvalidasi input nilai yang diberikan untuk defense
        if InputNum > 0 and isinstance(InputNum, int): # isinstance() digunakan untuk 
            self.__defense += InputNum                 # mengecek apakah InputNum bertipe
        else:
            print("masukkan nilai defense yang benar")
    
    @defense.deleter
    def defense(self):
        self.__defense = 0
        




#Kamado = Hero("Kamado Tanjirou", 100, 50)
Kyojuro = Hero1("Rengoku Kyojuro",100, 60)
Kyojuro.defense = 40
# memanggil getter (method)
#print(Kamado.getInfo())
#print(Kamado.__name)
#Kamado.name = "Akaza" 
#print(Kamado.__dict__)
#print(Kamado.getInfo())
# memangil property 
#print(Kyojuro.getInfo) # pemanggilan getInfo di bawah @property tidak perlu menggunakan ()
# mengubah nama Kyojuro
#Kyojuro.__name = "Akaza"
print(Kyojuro.getInfo)
#print(Kyojuro.__dict__)
# memangggil getter property
#print(Kyojuro.defense)
# memanggil setter property
#Kyojuro.defense = 10
#print(Kyojuro.defense)
#del Kyojuro.defense
#print(Kyojuro.defense)
#print(Kyojuro.getInfo)
#Kyojuro.defense = 60
#print(Kyojuro.getInfo)