from turtle import Screen, Turtle
import turtle
import pandas as pd

screen = Screen()
screen.title("U.S States Game")



image = './US_State_Game/blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv('./US_State_Game/50_states.csv')
state_list = data.state.to_list()

guessed_states = []
correct_poin = 0

while len(guessed_states) < len(state_list):

    answer_state = screen.textinput(title=f"{correct_poin}/50 States Correct", prompt="Whats another states name?").title()

    # check the answer
    if answer_state in state_list:
        correct_poin += 1
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        

screen.exitonclick()