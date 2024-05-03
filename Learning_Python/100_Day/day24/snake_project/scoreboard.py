from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.high_score = 0
        with open("data.txt") as file: 
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Hig Score: {self.high_score}", align=ALIGMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file: 
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        
    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write(f"GAME OVER", align=ALIGMENT, font=FONT)
        
    def scoring(self):
        self.score += 1
        self.update_scoreboard()
