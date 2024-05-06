# First, use list comprehension to convert the list_of_strings to a list of integers.
# Then use list comprehension again to create a new list called result.
#  This new list should only contain the even numbers from the list numbers.


list_of_strings = input("Input your numbers : ").split(',')
list_of_int = [int(i) for i in list_of_strings]
result = [n for n in list_of_int if n % 2 == 0]

print(result)