# make prime numbers program

def prime_checker(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    
    if is_prime == True:
        print(f"{number} is Prime number")
    else:
        print(f"{number} is not prime number")
        
n = int(input("Check this number : "))
prime_checker(number=n)