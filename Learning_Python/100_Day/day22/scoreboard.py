from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230 )
        self.write(f"{self.l_score}", align=ALIGMENT, font=FONT)
        self.goto(100, 230 )
        self.write(f"{self.r_score}", align=ALIGMENT, font=FONT)
    
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

        