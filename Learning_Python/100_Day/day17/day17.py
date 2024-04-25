# primitive way to create class
class User: # make the class
    pass    

user_1 = User() # make object
user_1.id = "001" # adding atribute
user_1.username = "Angela"

print(user_1.username)


# make more nice way
class Person:
    
    def __init__(self, person_id, username):
        print("new person is created...")
        self.id = person_id
        self.username = username
        self.followers = 0 # we can setting default value so its not always have to in parameters

person1 = Person("001", "Shalom")
print(person1.id)
print(person1.username)