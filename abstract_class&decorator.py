from abc import ABC, abstractclassmethod

class Button(ABC):

    def __init__(self, set_link):
        self.link = set_link

    @abstractclassmethod
    def click(self):
        pass

class PushButton(Button):
    
    """
        penulisan method click dengan link seperti di bawah ini
        memiliki kelemahan yaitu jika kita tidak mengetahui
        seperti apa abstrak class, program akan menjadi implisit
        dan mengurangi tingkat keterbacaan, kita akan bertanya-tanya
        darimana self.link berasal, ini bisa dihindari dengan membuat
        link menjadi property sekaligus abstract method yang nantinya 
        akan dipaksa untuk diimplementasikan ke class lainnya menggunakan
        getter dan setter
    
    """
    def click(self):
        print("go to: {}".format(self.link))


tombol = PushButton("www.youtube.com")
tombol.click()

class Button(ABC):

    def __init__(self, set_link):
        self.link = set_link

    @abstractclassmethod
    def click(self):
        pass

    @property
    @abstractclassmethod
    def link(self):
        pass


class PushButton(Button):
    
    """
        berikut adalah implementasi link menggunakan 
        getter dan setter
    
    """
    def click(self):
        print("go to: {}".format(self.link))
    
    # deklarasi class pemilik method link 
    # diperlukan sebelum membuat setter atau getter
    # deklarasi class dapat dipasangkan 
    # baik setter terlebih dahulu
    # atau getter terlebih dahulu, yang
    # penting deklarasi class berada di urutan pertama
    # sebelum pembutan getter atau setter selanjutnya

    @Button.link.setter
    def link(self, input):
        self.__link = input
    
    # untuk getter tidak diperlukan lagi 
    # deklarasi class dari pemilik method
    @link.getter
    def link(self):
        return self.__link

"""
    dengan mengimplementasikan method link sebagai property


"""

tombol = PushButton("www.youtube.com")
# mengganti link yang dituju dengan setter yang telah dibuat
tombol.link = "www.github.com"
tombol.click()