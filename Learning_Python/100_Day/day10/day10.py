# Function with output
def  my_function():
    result = 3 * 2
    return result

# make our function with output example

first_name = input("Inpur your first name : ")
last_name = input("Input your last name : ")

def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

print(format_name(first_name, last_name))