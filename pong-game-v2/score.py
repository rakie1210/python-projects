from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,250)
        self.write(self.l_score, align="center", font=("Courier", 24, "normal"))
        self.goto(100,250)
        self.write(self.r_score, align="center", font=("Courier", 24, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Courier", 24, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("Courier", 24, "normal"))

    def l_point(self):
        self.l_score +=1

    def r_point(self):
        self.r_score +=1