# oop
#import another_module
#print(another_module.another_variable)

#from turtle import Turtle, Screen
# make object
#tono = Turtle()
#print(tono)
#tono.shape("turtle")
#tono.color("green", "blue")
#tono.forward(200)

# screen is object
#my_screen = Screen()
#print(my_screen.canvheight) # canvheight is atribut

#my_screen.exitonclick() # exitonclick is method


# try to use package that allready exists in python comunity
# we should install the pacakge in python extensions

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

table.align = "l"
print(table)
