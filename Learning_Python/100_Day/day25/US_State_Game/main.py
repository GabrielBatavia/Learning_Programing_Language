from turtle import Screen
import turtle

screen = Screen()
screen.title("U.S States Game")



image = './US_State_Game/blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop() # keep our screen open

