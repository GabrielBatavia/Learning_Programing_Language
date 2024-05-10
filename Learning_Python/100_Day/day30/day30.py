# all errors

# FilenotFound
# with open("asdsa.txt") as file:
#    file.read()

# Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_exixstent_key"]

#IndexError
# fruit_list = ["apple"]
# fruit = fruit_list[3]

# Typeerror
# text = "abc"
# print(text + 4)


# Catching exceptions

try:
    with open("asdsa.txt") as file:
        file.read()
    a_dictionary = {"key": "value"}
    value = a_dictionary["non_exixstent_key"]

except FileNotFoundError:
    with open("asdsa.txt", mode="w") as file:
        file.write("asdsa.txt")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    print("The file open is successful")

finally:
    print("We are done")

print()


# checking fail logic and raise error

height = float(input("Height : "))
weight = float(input("Weight : "))

if height > 300:
    raise ValueError("Enter your height correctly")

bmi = weight / height
print(bmi)