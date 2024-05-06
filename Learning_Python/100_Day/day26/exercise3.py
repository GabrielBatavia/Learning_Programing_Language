# You are going to create a list called result which contains the numbers that are common in file1 and file2.

with open("file1.txt") as file1: 
    numbers1 = file1.readlines()

with open("file2.txt") as file2: 
    numbers2 = file2.readlines()
    
result = [int(n) for n in numbers1 if n in numbers2]

print(result)