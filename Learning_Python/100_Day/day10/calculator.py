# make calculator program

# add function 
def add(n1, n2):
    return n1 + n2

# Subtract function
def subtrack(n1, n2):
    return n1 - n2

# multiply function
def multiply(n1, n2):
    return n1 * n2

# divide function
def divide(n1, n2):
    return n1 / n2

# make dictionary for calculations
math_operator = {"+": add,
                 "-": subtrack,
                 "*": multiply,
                 "/": divide,}

# get input from user for our argument
num1 = int(input("Whats the first number? : "))
num2 = int(input("Whats the second number? : "))

for key in math_operator:
    print(key)

operation_symbol = input("Pick an operation from the line above: ")

# get choosen operation function and call it 
choosen_function = math_operator[operation_symbol]
result = choosen_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {result}")
