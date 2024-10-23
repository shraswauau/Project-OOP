# Praktek ke-3
# Membuat sebuah sistem restoran sederhana menggunakan OOP
# Interaksi antar objek

class MenuItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga 
        
    def __str__(self):
        return f"{self.nama} - ${self.harga:.2f}"
    
class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.pesanan = []
        
    def pesan(self, menu_item):
        self.pesenan.append(menu_item)
        print(f"{self.nama} memesan {menu_item}")
        
    def bayar(self):
        total = sum(item.harga for item in self.pesanan)
        return total
    
class Pelayan:
    def __init__(self, nama):
        self.nama = nama
        
    def ambil_pesanan(self, pelanggan):
        print(f"{self.nama} mengambil pesanan dari {Pelanggan.nama}")
    
    def antar_pesanan(self, pelanggan):
        total = Pelanggan.bayar()
        print(f"{self.nama} mengantarkan pesanan kepada {Pelanggan.nama}")
        print(f"Total tagihan: ${total:.2f}")
        
class Dapur:
    def __init__(self):
        self.menu = {
            "mie": MenuItem("mie", 5.99),
            "martabak": MenuItem("martabak", 7.99),
            "wonton": MenuItem("wonton", 8.99)
        }
        
    def siapkan_pesanan(self, pesanan):
        for item in pesanan:
            if item.nama in self.menu:
             print(f"Menyediakan {item} dengan harga ${item.harga:.2f}")
            else:
                print(f"{item.nama} tidak ada dalam menu")
                
Pelanggan = Pelanggan("muthia")
Pelayan = Pelayan("sahara")
Dapur = Dapur()
                
mie = MenuItem("mie", 5.99)
wonton = MenuItem("wonton", 8.99)
                
Pelanggan.pesan(mie)
Pelanggan.pesan(wonton)
                
Pelayan.ambil_pesanan(Pelanggan)
Dapur.siapkan_pesanan(Pelanggan.pesanan)
                
Pelayan.antar_pesanan(Pelanggan)