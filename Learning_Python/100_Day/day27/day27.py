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