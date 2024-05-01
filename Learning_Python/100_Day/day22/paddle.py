from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=0.5)
    
    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)
        
    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)