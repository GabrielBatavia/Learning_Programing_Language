from turtle import Turtle

class Paddle:
    
    def __init__(self):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=3, stretch_len=0.5)
        self.paddle.goto(350, 0)
    
    def go_up(self):
        self.new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)
        
    def go_down(self):
        self.new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)