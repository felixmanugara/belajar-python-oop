# object oriented programming adalah paradigma pemograman 
# yang mana memperlakukan semua bagian program seperti objek
# yang masing-masing memiliki atributnya tersendiri

# class biodata digunakan untuk menginisiasi sebuah class bernama biodata
class Hero:
   pass

# PERSON merupakan inisiasi objek dari class biodata
PERSON1 = Hero() # object / instance
PERSON2 = Hero()
PERSON3 = Hero()

# kedua syntax di bawah merupakan atribut dari objek PERSON
PERSON1.name = "Rengoku Kyojuro"
PERSON1.health = 100
PERSON1.ability = "Speed, Fire Breathing"

PERSON2.name = "Akaza"
PERSON2.health = 100
PERSON2.ability = "Physical Strength, Blood Demon Art "

PERSON3.name = "Kamado Tanjirou"
PERSON3.health ="100"
PERSON3.ability = "Sharp Smell,Water Breathing "

# __dict__ digunakan untuk menunjukkan atribut apa saja yang dimiliki oleh suatu objek
print(PERSON1.__dict__)
print(PERSON2.__dict__)
print(PERSON1.name)
print(PERSON2.ability)

# program di atas belum sepenuhnya mereprensetasikan penggunaan oop secara ideal
# program di atas hanya digunakan untuk mengambarkan konsep dari oop




