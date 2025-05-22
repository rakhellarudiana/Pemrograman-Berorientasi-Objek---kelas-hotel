#Membuat Project Pemrograman Berorientasi Objek (yang ada class seperti objek, atribut, method) Dan Dapat Dipakai Dalam Sehari-hari)
#CLASSES
#cara pada nomor 1
class Hotel:
    klasifikasi_hotel_bintang_1      = 'bintang 1'
    persyaratan_hotel_bintang_1      = 'minimum jumlah 15 kamar standar, kamar mandi dalam, luas kamar standar minimum 20m²'
    klasifikasi_hotel_bintang_2      = 'bintang 2'
    persyaratan_hotel_bintang_2      = 'minimum jumlah 20 kamar standar, 1 kamar suit dan kamar mandi dalam, luas kamar standar minimum 22m² dan luas kamar suit minimum 44m²'
    klasifikasi_hotel_bintang_3      = 'bintang 3'
    persyaratan_hotel_bintang_3      = 'minimum jumlah 30 kamar standar, 2 kamar suit dan kamar mandi dalam, luas kamar standar minimum 24m² dan luas kamar suit minimum 48m²'
    klasifikasi_hotel_bintang_4      = 'bintang 4'
    persyaratan_hotel_bintang_4      = 'minimum jumlah 50 kamar standar, 3 kamar suit dan kamar mandi dalam, luas kamar standar minimum 24m² dan luas kamar suit minimum 48m²'
    klasifikasi_hotel_bintang_5      = 'bintang 5'
    persyaratan_hotel_bintang_5      = 'minimum jumlah 100 kamar standar, 4 kamar suit dan kamar mandi dalam, luas kamar standar minimum 26m² dan luas kamar suit minimum 52m²'
hotel = Hotel()
print('-- class Hotel --')
print('memiliki 2 objek Hotel: ')
print('klasifikasi hotel bintang 1  : ', hotel.klasifikasi_hotel_bintang_1)
print('persyaratan hotel bintang 1  : ', hotel.persyaratan_hotel_bintang_1)
print('klasifikasi hotel bintang 2  : ', hotel.klasifikasi_hotel_bintang_2)
print('persyaratan hotel bintang 2  : ', hotel.persyaratan_hotel_bintang_2)
print('klasifikasi hotel bintang 3  : ', hotel.klasifikasi_hotel_bintang_3)
print('persyaratan hotel bintang 3  : ', hotel.persyaratan_hotel_bintang_3)
print('klasifikasi hotel bintang 4  : ', hotel.klasifikasi_hotel_bintang_4)
print('persyaratan hotel bintang 4  : ', hotel.persyaratan_hotel_bintang_4)
print('klasifikasi hotel bintang 5  : ', hotel.klasifikasi_hotel_bintang_5)
print('persyaratan hotel bintang 5  : ', hotel.persyaratan_hotel_bintang_5)

print()

#CLASSES N OBJECT (KELAS N OBJEK)
#cara pada nomor 2
class Hotel:
    kelas_1                     = 'kelas paling rendah'
    klasifikasi_hotel_bintang_1 = 'bintang 1'
    persyaratan_hotel_bintang_1 = 'minimum jumlah 15 kamar standar, kamar mandi dalam, luas kamar standar minimum 20m²'
    kelas_2                     = 'kelas rendah'
    klasifikasi_hotel_bintang_2 = 'bintang 2'
    persyaratan_hotel_bintang_2 = 'minimum jumlah 20 kamar standar, 1 kamar suit dan kamar mandi dalam, luas kamar standar minimum 22m² dan luas kamar suit minimum 44m²'
    kelas_3                     = 'kelas menengah'
    klasifikasi_hotel_bintang_3 = 'bintang 3'
    persyaratan_hotel_bintang_3 = 'minimum jumlah 30 kamar standar, 2 kamar suit dan kamar mandi dalam, luas kamar standar minimum 24m² dan luas kamar suit minimum 48m²'
    kelas_4                     = 'kelas atas'
    klasifikasi_hotel_bintang_4 = 'bintang 4'
    persyaratan_hotel_bintang_4 = 'minimum jumlah 50 kamar standar, 3 kamar suit dan kamar mandi dalam, luas kamar standar minimum 24m² dan luas kamar suit minimum 48m²'
    kelas_5                     = 'kelas paling atas'
    klasifikasi_hotel_bintang_5 = 'bintang 5'
    persyaratan_hotel_bintang_5 = 'minimum jumlah 100 kamar standar, 4 kamar suit dan kamar mandi dalam, luas kamar standar minimum 26m² dan luas kamar suit minimum 52m²'
#membuat objek dari kelas makanan
kelas = Hotel()
print('-- class Hotel --')
print('memiliki 5 kelompok Hotel
      : ')
print('kelas 1                     : ', kelas.kelas_1)
print('klasifikasi hotel bintang 1 : ', kelas.klasifikasi_hotel_bintang_1)
print('persyaratan hotel bintang 1 : ', kelas.persyaratan_hotel_bintang_1)
print('kelas 2                     : ', kelas.kelas_2)
print('klasifikasi hotel bintang 2 : ', kelas.klasifikasi_hotel_bintang_2)
print('persyaratan hotel bintang 2 : ', kelas.persyaratan_hotel_bintang_2)
print('kelas 3                     : ', kelas.kelas_3)
print('klasifikasi hotel bintang 3 : ', kelas.klasifikasi_hotel_bintang_3)
print('persyaratan hotel bintang 3 : ', kelas.persyaratan_hotel_bintang_3)
print('kelas 4                     : ', kelas.kelas_4)
print('klasifikasi hotel bintang 4 : ', kelas.klasifikasi_hotel_bintang_4)
print('persyaratan hotel bintang 4 : ', kelas.persyaratan_hotel_bintang_4)
print('kelas 5                     : ', kelas.kelas_5)
print('klasifikasi hotel bintang 5 : ', kelas.klasifikasi_hotel_bintang_5)
print('persyaratan hotel bintang 5 : ', kelas.persyaratan_hotel_bintang_5)

print()

#cara pada nomor 3
#membuat kelasnya terlebih dahulu
class Hotel:
    klasifikasi_hotel_bintang = None
    persyaratan_hotel_bintang = None
    def mengetahui (self):
        print(f"mengetahui klasfikasi hotel bintang {self.klasifikasi_hotel_bintang} dan persyaratan hotel bintang {self.persyaratan_hotel_bintang}")
bintang_3                           = Hotel()
bintang_3.klasifikasi_hotel_bintang = "bintang 3"
bintang_3.persyaratan_hotel_bintang = "minimum jumlah 30 kamar standar, 2 kamar suit dan kamar mandi dalam, luas kamar standar minimum 24m² dan luas kamar suit minimum 48m²"
bintang_1                           = Hotel()
bintang_1.klasifikasi_hotel_bintang = "bintang 1"
bintang_1.persyaratan_hotel_bintang = "minimum jumlah 15 kamar standar, kamar mandi dalam, luas kamar standar minimum 20m²"
#panggil fungsi mengenali
bintang_3.mengetahui()
bintang_1.mengetahui()

print()

#cara pada nomor 4
#metodenya
class Hotel:
    def __init__(self, kelas, klasifikasi_hotel, persyaratan_hotel):
        self.kelas             = kelas             #atribut tingkat
        self.klasifikasi_hotel = klasifikasi_hotel #atribut klasfikasi hotel
        self.persyaratan_hotel = persyaratan_hotel #atribut persyaratan hotel
    def tampilkan_kelas(self):
        print(f"kamar kelas hotel ini {self.kelas}")
    def tampilan_info(self):
        print(f"hotel ini kelas {self.kelas}, dengan klasifikasi hotel {self.klasifikasi_hotel}, serta persyaratan hotel {self.persyaratan_hotel}")
#membuat objek
hotel = Hotel("kelas rendah", "bintang 2", "minimum jumlah 20 kamar standar, 1 kamar suit dan kamar mandi dalam, luas kamar standar minimum 22m² dan luas kamar suit minimum 44m²")
#mengakses atribut
print(hotel.kelas)             #output: kelas rendah
print(hotel.klasifikasi_hotel) #output: bintang 2
print(hotel.persyaratan_hotel) #output: minimum jumlah 20 kamar standar, 1 kamar suit dan kamar mandi dalam, luas kamar standar minimum 22m² dan luas kamar suit minimum 44m²
#memanggil metode
hotel.tampilkan_kelas()
hotel.tampilan_info()

print()

#INHERITANCE (PENURUNAN)
#cara pada nomor 5
#Kelas Induk
class Hotel:
    def __init__(self, kelas, klasifikasi_hotel, persyaratan_hotel):
        self.kelas             = kelas          
        self.klasifikasi_hotel = klasifikasi_hotel
        self.persyaratan_hotel = persyaratan_hotel
    def tampilan_info(self):
        print(f"hotel ini kelas {self.kelas} dengan klasifikasi hotel {self.klasifikasi_hotel}, serta persyaratan hotel {self.persyaratan_hotel}")
#Kelas Turunan (Kelas Hotel Bintang 4)
class Bintang_4(Hotel):
    def __init__ (self, kelas, klasifikasi_hotel, persyaratan_hotel):
        super().__init__(kelas, klasifikasi_hotel, persyaratan_hotel)
        self.kelas             = kelas          
        self.klasifikasi_hotel = klasifikasi_hotel
        self.persyaratan_hotel = persyaratan_hotel
    def tampilan_informasi(self):
        return f"hotel ini kelas {self.kelas}, dengan klasifikasi hotel {self.klasifikasi_hotel}, serta persyaratan hotel {self.persyaratan_hotel}"
#Kelas Turunan (Kelas Hotel Bintang 5)
class Bintang_5(Hotel):
    def __init__ (self, kelas, klasifikasi_hotel, persyaratan_hotel):
        super().__init__(kelas, klasifikasi_hotel, persyaratan_hotel)
        self.kelas             = kelas          
        self.klasifikasi_hotel = klasifikasi_hotel
        self.persyaratan_hotel = persyaratan_hotel
    def tampilan_informasi(self):
        return f"kelas hotel bintang {self.kelas}, dengan klasifikasi hotel {self.klasifikasi_hotel}, serta persyaratan hotel {self.persyaratan_hotel}"
#Membuat objek dan mencetak informasi
bintang_1 = Bintang_4("kelas atas", "bintang 4", "minimum jumlah 50 kamar standar, 3 kamar suit dan kamar mandi dalam, luas kamar standar minimum 24m² dan luas kamar suit minimum 48m²")
print(bintang_1.tampilan_informasi())
bintang_2 = Bintang_5("kelas paling atas", "bintang 5", "minimum jumlah 100 kamar standar, 4 kamar suit dan kamar mandi dalam, luas kamar standar minimum 26m² dan luas kamar suit minimum 52m²")
print(bintang_2.tampilan_informasi())

print()

#ENCAPSULATION N POLYMORPHISM (PENGKAPSULASI / PENGKAPSULAN N POLIMORFISME)
#PENGKAPSULAN / PENGKAPSULASI(ENCAPSULATION)
#cara pada nomor 6
class Hotel:
    def __init__(self, kelas=0):
        #Atribut private, tidak dapat diakses langsung dari luar kelas
        self.__kelas = kelas
#metode untuk menambah nilai kelas Hotel
    def tambah_kelas(self, amount):
        if amount > 0:
            self.__kelas += amount
            return f"berhasil menambah {amount}. nilai kelas hotel: {self.__kelas}"
        else:
            return "jumlah nilai kandungan tidak valid!"
#metode untuk mengurangi nilai kelas Hotel
    def kurangi_kelas(self, amount):
        if 0 < amount <= self.__kelas:
            self.__kelas -= amount
            return f"berhasil mengurangi {amount}. nilai kelas hotel: {self.__kelas}"
        else:
            return "jumlah nilai kelas hotel tidak valid atau melebihi jumlah yang tersedia!"
#metode untuk check nilai kelas Hotel
    def cek_kelas(self):
        return f"nilai kelas hotel: {self.__kelas}"
#membuat objek dari kelas Hotel
hotel1 = Hotel()
#menambah nilai kelas Hotel
print(hotel1.tambah_kelas(3))  #"berhasil menambah . nilai kelas hotel sekarang: "
#mengecheck nilai kelas Hotel
print(hotel1.cek_kelas())      #"nilai kelas hotel: "
#mengurangi nilai kelas Hotel
print(hotel1.kurangi_kelas(1)) #"berhasil mengurangi . nilai kelas hotel sekarang: "

print()

#POLIMORFISME
#cara pada nomor 7
class Bintang_1:
    def persyaratan_hotel_bintang(self):
        return "minimum jumlah 15 kamar standar, 1 kamar dan kamar mandi dalam, luas kamar standar minimum 20m2"
class Bintang_4:
    def persyaratan_hotel_bintang(self):
        return "minimum jumlah 50 kamar standar, 3 kamar suit dan kamar mandi dalam, luas kamar standar minimum 24m² dan luas kamar suit minimum 48m2"
#fungsi
def persyaratan_dalam_hotel_Bintang_1_dan_Bintang_4(hotel):
    print(hotel.persyaratan_hotel_bintang())
#membuat objek dari kelas Bintang 1 dan Bintang 4
luas_kamar_standar_minimum_20m2                                  = Bintang_1()
luas_kamar_standar_minimum_24m2_dan_luas_kamar_suit_minimum_48m2 = Bintang_4()
#memanggil fungsi persyaratan dalam hotel Bintang 1 dan Bintang 4
persyaratan_dalam_hotel_Bintang_1_dan_Bintang_4(luas_kamar_standar_minimum_20m2)
persyaratan_dalam_hotel_Bintang_1_dan_Bintang_4(luas_kamar_standar_minimum_24m2_dan_luas_kamar_suit_minimum_48m2)
