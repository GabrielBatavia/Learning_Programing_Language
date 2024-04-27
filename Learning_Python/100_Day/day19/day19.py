from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)     # set up scrre

# make the pop up screen
user_bet = screen.textinput(title="Make your bet", prompt="Which tutle win the race? Enter your color choose : ")
print(f"You bet a {user_bet}")
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
Y_post = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tono = Turtle(shape="turtle")
    tono.color(colors[turtle_index])
    tono.penup()
    tono.goto(x=-230, y=Y_post[turtle_index])



#def move_forwards():
#    tono.forward(10)

#def move_backwards():
#    tono.backward(10)

#def move_left():
#    tono.left(10)

#def move_right():
#    tono.right(10)
    
#def clear():
#    tono.clear()
#    tono.penup()
#    tono.home()
#    tono.pendown()

















screen.listen()
#screen.onkey(key="w", fun=move_forwards)
#screen.onkey(key="s", fun=move_backwards)
#screen.onkey(key="a", fun=move_left)
#screen.onkey(key="d", fun=move_right)
#screen.onkey(key="c", fun=clear)
screen.exitonclick()