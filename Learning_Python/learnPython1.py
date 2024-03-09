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

print()

print('aaa' in 'aaa-bbb-ccc')
print('bbb' in 'aaa-bbb-ccc')
print('ddd' in 'aaa-bbb-ccc')

print()

age = 18 # diberikan kondisi bahwa age = 18

if age < 20: # result dari age < 20 adalah True
    print('youth discount')

num = 2
if num % 2 == 0:
    print('Nomor genap')
if num % 3 == 0:
    pass
    print("nomor AKUH")

print("nomor")

print()

num = -100
if num < 0:
    print(num, 'adalah bilangan negatif. ')
else:
    print(num, 'adalah bukan bilangan negatif ')
    if num % 2 == 0:
        print(num, 'adalah bilangan genap')
    else:
        print(num, 'adalah bilangan ganjil')
        

for i in range(5):
    print('Welcome to everyone!!')
    
x = {'a': 0, 'b': 0 , 'c': 0, 'd': 0}
y = x.copy()

print(x is y) # cek apakah kedua dictionary merupakan objek yang sama
print(x == y) # cek apakah key-value pairnya sama

x = {'a': {'python':'2.7'},'b':{'python':'3.6'}}
y = x.copy()

y['a']['python'] = '2.7.15' # merubah value dari key a - python
print(x)
print(y)


import copy
#syntax

x = {'a': {'python':'2.7'},'b':{'python':'3.6'}}
import copy # memanggil copy module
y = copy.deepcopy(x) # deep copy menggunakan deepcopy function dari copy module

y['a']['python'] = '2.7.15' # merubah value dari key a - python
print(x)
print(y)


from collections import defaultdict # import default dict method dari collections module

keys = ('a','b','c','d')
y = dict.fromkeys(keys,100)
y = defaultdict(int) # set default value sebagai integer

print(y['z']) # mengakses key z dari dictionary y


keys = ['a','b','c','d']
x = dict.fromkeys(keys, 1000)
print(x)

days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' , 'Sun' ] # list
days_set = set(days_list) # membuat set dari list
print(days_set)

fruits_tuple = ('apple','orange','water melon')
fruits_set = set(fruits_tuple) # membuat set dari tuple
print(fruits_set)

numbers = {2,1,3}
for x in numbers:
  print(x)

numbers = {2,1,3}
if 1 in numbers:
  print("1 terdapat dalam set")