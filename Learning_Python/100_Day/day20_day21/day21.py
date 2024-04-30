# Class inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal): # (Animal) is for call the parents class
    def __init__(self):
        super().__init__() # to define that we get all the attributs and method from the parents to the child
    
    # if we want add or modify the method
    def breathe(self):
        super().breathe()
        print("Doing this underwater")
        
    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)