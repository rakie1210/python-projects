"""A Class to show the scoreboard of the snake game."""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "italic")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 278)
        self.write(f"Score:{self.score}", move= True,align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear_score()
        self.score += 1
        self.write(f"Score:{self.score}", move= True,align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear_score()
        self.goto(0, 0)
        self.write(f"Game Over! Your score is {self.score}", move= True,align=ALIGNMENT, font=FONT)

    def clear_score(self):
        self.clear()
        self.goto(0, 278)