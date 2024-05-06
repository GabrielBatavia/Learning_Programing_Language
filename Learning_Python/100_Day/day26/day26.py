# List comprehension

# Reguler way
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    n += 1
    new_list.append(n)

print(new_list)

# list comprehension way
## new_list = [new_item for item in list]
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

print(new_list)

print()


# list comprehension with string
name = "Shalom"
new_name = [letter for letter in name]

print(new_name)


# with range
new_range = [n * 2 for n in range(1, 5)]
print(new_range)


# Conditional list comprehension
## new_list = [new_item for item in list if test]

names = ["Shalom", "Linda", "Syafa", "Nia", "Putri"]
friends = [name.upper() for name in names if len(name) > 4]

print(friends)


# Dictionary Comprehension
## new_dictionary = {new_key:new_value for (key, value) in dict.items()}

# Conditional dictionary comprehension
## new_dictionary = {new_key:new_value for (key, value) in dict.items() if test}

import random

names = ["Shalom", "Linda", "Syafa", "Nia", "Putri"]
student_score = {student:random.randint(1,100) for student in names}

print(student_score)
print()

passed_student = {student:score for (student, score) in student_score.items() if score > 60}

print(passed_student)