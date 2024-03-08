print("Hello Sekai !!!" * 10)
print(1+2)

teks = "halo, nama saya, budi"
x = teks.split(", ")
print(x)

#islower() -> Digunakan untuk mengecek apakah semua element dalam string adalah huruf kecil, akan mengembalikan True jika iya, dan False jika tidak
a = "HaLo"
b = "halo"

print(a.islower())
print(b.islower())

#count()-> Digunakan untuk menghitung berapa kali sebuah value muncul dalam sebuah string
teks = "Halo semuanya, disini saya bersama dengan budi semuanya"
x = teks.count("semuanya")
print(x)

print(100//20)

#int() -> Digunakan untuk mengubah nilai yang ditentukan menjadi bilangan bulat. Contohnya:
x = int("12")
y = int(12.5)

print(x)
print(y)

#output
#12
#12

#pow() -> Digunakan untuk mendapatkan nilai pangkat dari suatu bilangan. Contohnya:
x = pow(3, 3) # 3 pangkat 3
y = pow(3, -3) # 3 pangkat -3

print(x)
print(y)

#output
#27
#0.015625

#str() -> Digunakan untuk mengubah sebuah objek menjadi string. Contohnya:
x = str(12)
y = str(12.5)

print(type(x))
print(type(y))

#output
#<class 'str'>
#<class 'str'>

lebar = 10 # identifier untuk membedakan lebar persegi panjang dari data lain
tinggi = 5 # identifier untuk membedakan tinggi persegi panjang dari data lain
luas_kotak = lebar * tinggi
print('luas area kotak = ', luas_kotak)

#global1 = 10 

print('aaa' == 'aaa')
print('aaa'== 'bbb')
print('aaa' != 'aaa')
print('aaa' != 'bbb')

#output
True
False
False
True

a = 1
b = 1.0
print(a == b)
print(a is b)

# output
True
False