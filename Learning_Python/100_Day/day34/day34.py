# Typing data tipe
age: int


age = 12
print(age)


# Type Hints

# make expected input in some datatype
# -> make expected output in some datatype
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
        
    return can_drive

police_check(19)
