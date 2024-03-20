def menyapaPelanggan(*names):
    for name in names:
        print ('Halo', name, 'Selamat Datang Ditoko Kami')
        
    return(names)

menyapaPelanggan('Anna', 'Clara', 'Gabriel')

names = input('Masukkan Nama Anda : ')

menyapaPelanggan(names)

def redmi(namaProduk, harga):
    print("Selamat Anda Telah Membeli")
    
    print("Handphone yang anda beli : " , namaProduk)
    print("Harga yang anda beli     : " , str(harga))
    return(namaProduk, harga)

namaProduk = input("Masukkan nama Handphone yang anda ingin beli : ")
harga = float(input("Masukkan harga Handphone yang anda ingin dibeli   : "))

redmi(namaProduk, harga)


def laptop(namaProduk, harga):
    print("Selamat Anda Telah Membeli")
    
    print("Laptop yang anda beli : " , namaProduk)
    print("Harga yang anda beli     : " , str(harga))
    return(namaProduk, harga)

namaProduk = input("Masukkan nama Handphone yang anda ingin beli : ")
harga = float(input("Masukkan harga Handphone yang anda ingin dibeli   : "))


