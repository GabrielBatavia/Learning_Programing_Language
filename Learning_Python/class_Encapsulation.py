#Single Underscore
class Orang:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age
 
    def tampilkan(self):
        print(self.name)
        print(self._age)
 
orang_obj = Orang('Budi', 30)

#mengakses melalui metode
orang_obj.tampilkan()

#mengakses langsung variable
print(orang_obj.name)
print(orang_obj._age)



#Double Underscore
class Orang:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
 
    def tampilkan(self):
        print(self.name)
        print(self.__age)
 
orang_obj = Orang('Budi', 30)

#mengakses melalui metode
orang_obj.tampilkan()

#mengakses langsung variable
print(orang_obj.name)
#print(orang_obj.__age)




#
class Orang:
  def __init__(self, name, age=0):
    self.name = name
    self.__age = age

  def setAge(self, age):
    self.__age = age
 
  def tampilkan(self):
    print(self.name)
    print(self.__age)
    print("----------")
 
orang_obj = Orang('Budi', 30)

#mengakses melalui metode
orang_obj.tampilkan()

#mengubah data tanpa setter tidak memungkinkan
orang_obj.__age = 50
orang_obj.tampilkan()

#mengubah data harus memalui setter
orang_obj.setAge(27)
orang_obj.tampilkan()