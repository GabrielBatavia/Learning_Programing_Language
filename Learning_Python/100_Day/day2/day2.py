# Data Types

# String
print("Hallo")
print('Hallo'[0])
print('Hallo'[-1])

# Integer
a = 10
b = 15
c = a + b
print(c)

print(123 + 345)

print(123_456_678)

# Float 

d = 3.14159
print(d)

# Boolean
True
False

print(True)
print(False)


# Check the type of data

print(type(a))

print(type(d))

# Change the type of data

a = str(a)
print("Hallo you number " + a)
print(type(a))

a = int(a)
print(a + c)
print(type(a))

# Math operations

print(3 + 4)
print(3 - 4)
print(3 / 4)
print(3 * 4)
print(3 % 4)
print(3 ** 4)

print(3 * (3 + 3) / 3 - 3)

# Number manipulation
print(8 / 3)
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2)) # number after come is for decide number of place in round
print(round(8 / 3, 3))

print(8 // 3) # Will make without float numbers

result = 4 / 2
result /= 2 # short hand instaed make result = result / 2
print(result)


# F String

# this primitive way and painful
score = 0
print("your score is", str(score))

height = 1.8
isWinning = True

# use F string
print(f"your score is {score}, your heightis {height}, and you are winning is {isWinning}")

