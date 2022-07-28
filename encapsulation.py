"""
Encapsulation / encapsulasi adalah sebuah mekanisme yang digunakan
untuk membatasi akses terhadapa artibut atribut yang terdapat pada 
sebuah objek, seperti pengguna tidak dapat mengakses nilai dari 
variabel yang dimiliki oleh objek, encapsulasi dapat digunakan untuk
menyembunyikan data yang terasosiasikan dengan class atau object

"""

class Hero:

    def __init__(self, Name, Health):
        self.__name = Name
        self.__health = Health

    # make getter for accessing private variable from outside class
    def getHealth(self):
        return self.__health

    # make getter for manipulating private variable from outside class
    def healthUp(self, addHealth):
        self.__health += addHealth

Rengoku = Hero("Rengoku",100)
# will raise error because we try to access private variable from outside class
#print(Rengoku.__name)
# use getHealth() to access private variable
print(Rengoku.getHealth())
# will raise error if we try to manipulate private variable from outside class
#Rengoku.__health += 300
# use healthUp() to change private variable value
Rengoku.healthUp(5)
print(Rengoku.getHealth())
