def redmi(namaProduk, harga):
    print("Selamat Anda Telah Membeli")
    
    print("Handphone yang anda beli : " + namaProduk)
    print("Harga yang anda beli     : " + str(harga))
    return(namaProduk, harga)

namaProduk = input("Masukkan nama Handphone yang anda ingin beli : ")
harga = float(input("Masukkan harga Handphone yang anda ingin dibeli   : "))

redmi(namaProduk, harga)