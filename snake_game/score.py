"""A Class to show the scoreboard of the snake game."""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "italic")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 278)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 278)
        self.write(f"Score:{self.score} High Score: {self.high_score}", move=True, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.clear_score()
    #     self.goto(0, 0)
    #     self.write(f"Game Over! Your score is {self.score}", move= True,align=ALIGNMENT, font=FONT)

    def clear_score(self):
        self.clear()
        self.goto(0, 278)