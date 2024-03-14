
class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()

obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()



#make a loop in tuple

class Hewan():
    def suara(self):
      print("Suara hewan")

class Kucing(): 
    def suara(self):
       print("Meow")

    def harapan_hidup(self): 
      print("Harapan hidup kucing adalah 10 tahun.") 
   
    def warna_tubuh(self): 
      print("Warna tubuh kucing pada umumnya adalah kuning") 
   
class Anjing(): 
    def suara(self):
      print("Woof")

    def harapan_hidup(self): 
      print("Harapan hidup anjing adalah 15 tahun.") 
   
    def warna_tubuh(self): 
      print("Warna tubuh anjing pada umumnya adalah hitam") 