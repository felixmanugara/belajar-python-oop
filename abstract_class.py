"""
    class abstrak adalah class yang menjadi
    blueprint dari class lainnya, bukan blueprint
    dari objek seperti class biasa, class abstrak 
    akan memaksa class lain untuk mengimplementasikan 
    method yang dimiliki oleh class abstrak tersebut, 
    dalam penjelasan lain kita tidak dapat membuat 
    instance berupa objek pada class abstrak

"""
# membuat abstract class
# abc = abstract base class
from abc import ABC,abstractclassmethod

class Button(ABC):
    # decorator @abstractclassmethod
    # berfungsi untuk memaksa method
    # dibawahnya untuk diimplementasikan
    # pada class lainnya
    @abstractclassmethod
    def click(self):
        pass

class PushButton(Button):

    def click(self):
        print("Push Button Click")
    
class RadioButton(Button):

    def click(self):
        print("Radio Button Click")

Tombol = PushButton()
Tombol2 = RadioButton()
Tombol3 = Button()
# Button adalah class abstract tidak bisa di instansiate 
"""
   abstract class cocok diterapkan pada sesuatu yang sifatnya masih
   belum jelas, seperti class button yang mana masih belum jelas seperti
   apa tipe tombolnya apakah ditekan, apakah radio, tetapi button memiliki
   kesamaan perilaku.

"""
print(Tombol3)

# class biasa dengan inheritance
class Button:
    
    def click(self):
        pass

class PushButton(Button):

    def click(self):
        print("Push Button Click")
    
class RadioButton(Button):

    def click(self):
        print("Radio Button Click")

Tombol = PushButton()
Tombol2 = RadioButton()
Tombol3 = Button()
