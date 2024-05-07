# Unlimited arguments

## def add(*args):
##  for n in args:
##      print(n)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
        
print(add(10, 10, 1))


#**kwargs , naby keyworded arguments

def calculate(n, **kwargs):
    
    print(type(kwargs))
    print(kwargs)
    
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=10)


class Car:
    
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.price = kw.get("price") # make it not cuase error if not in parameter

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.price)