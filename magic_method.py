class Food:
    """
        magic method adalah method bawaan
        dari python berikut beberapa contohnya 
    
    """
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    """ __repr__ adalah method bawaan yang digunakan
        untuk merepresentasikan objek dari sebuah
        class ke dalam tipe data string """
    def __repr__(self):
        rep = "Ini adalah class Food dengan objek {} berjumlah {}".format(self.nama, self.jumlah)
        return rep

    def __str__(self):
        string = "Ini adalah class Food dengan objek {} berjumlah {}".format(self.nama, self.jumlah)
        return string
    
    """ __add__ digunakan untuk menjumlahkan nilai 
        dari attribut yang ada pada sebuah object"""
    def __add__(self,object):
        return self.jumlah + object.jumlah


    def __dict__(self):
        return " ini adalah objek dari class makanan"

tahu = Food("Tahu",10)
tempe = Food("Tempe",5)

""" jika tidak mengunakan method __repr__ atau __str__ 
    maka output dari syntax di bawah bukan berupa 
    attribut objek melainkan class objek dan lokasi pada memori  """
""""
print(tahu) # atau print(repr(tahu))
# perlu diketahui bahwa output dari kedua syntax di bawah adalah sama
print(tempe.__str__())
print(tahu.__repr__())
print(tempe)

# menambahkan jumlah pada objek tahu dan tempe
print(tahu + tempe)
print(tahu.__dict__)
"""
print(tahu.__dict__())