# pada bagian ini akan dijelaskan penggunaan constructor __init__()
# __init__() berisi intruksi yang akan dieksekusi otomatis
#  pada saat menginisiasi objek dari sebuah class 

class Hero:
     def __init__(self,InputName,InputHealth,InputPower,InputDefense):
         self.Name = InputName # function parameter dijadikan atribut dari objek
         self.Health = InputHealth
         self.Power = InputPower
         self.Defense = InputDefense

         """
         self merupakan wujud dari class dalam
         contoh ini class Hero akan diinisiasi 
         dan dan diisi, dengan instance atau objek

         """

# inisiasi objek dari Hero
HERO1 = Hero("Rengoku Kyojuro",100,15,20) # Hero1 merupakan instance dari class Hero
HERO2 = Hero("Akaza",100,18,10)
HERO3 = Hero("Kamado Tanjirou",100,10,8)

print(HERO1.__dict__)
print(HERO2.Health)
print(HERO3.Defense)

"""
nantinya instance yang telah dibuat dapat memiliki atirbut dan behavior masing - masing
dengan menggunakan constructor __init__() penulisan kode program
cendrung lebih singkat dan membuatnya lebih mudah dibaca

"""
# dengan menggunakan constructor __init__() penulisan kode program
# cendrung lebih singkat dan membuatnya lebih mudah dibaca