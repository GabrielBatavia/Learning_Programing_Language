# Learn about dictinoary

programming_dictionary = {
    "Bug": "An error in program",
    "Function": "A piece of code that you can easily call over and over agian",
    "Loop": "The action of doing something over and over again"
}

print(programming_dictionary["Bug"])

#Add new items to dictinonary
programming_dictionary["Gabriel"] =  "The greatest man in world"

print(programming_dictionary)

# creating dictionary
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)


# edit an item in a dictionary
programming_dictionary["Bug"] = "Bug is suck"
print(programming_dictionary["Bug"])

# Loop throug a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])
    
