"""The file contains the class definition for the food of the snake"""

from turtle import Turtle, Shape, Screen
import random

# Mouse drawn facing right, centered on (0, 0)
BODY = ((-8, 0), (-6, 4), (-2, 5), (3, 4), (7, 2), (9, 0),
        (7, -2), (3, -4), (-2, -5), (-6, -4))
EAR = ((1, 4), (2, 8), (5, 8), (6, 5))
EYE = ((5, 1), (6, 2), (7, 1), (6, 0))
TAIL = ((-7, 1), (-12, 3), (-17, 2), (-19, -1),
        (-17, 1), (-12, 1), (-7, -1))
# Middle of the tail, measured from the mouse's center
TAIL_CENTER = (-13, 1)


def register_mouse_shape():
    """Builds a mouse out of polygons and registers it as the "mouse" shape"""
    mouse = Shape("compound")
    mouse.addcomponent(TAIL, "pink", "pink")
    mouse.addcomponent(BODY, "gray", "gray")
    mouse.addcomponent(EAR, "pink", "gray")
    mouse.addcomponent(EYE, "black", "black")
    Screen().register_shape("mouse", mouse)


class Food(Turtle):
    def __init__(self):
        #Inheriting from the Turtle class
        super().__init__()
        register_mouse_shape()
        self.shape("mouse")
        # Heading 90 shows the shape exactly as drawn above (facing right)
        self.setheading(90)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def tail_position(self):
        """Returns the screen position of the middle of the mouse's tail."""
        return self.xcor() + TAIL_CENTER[0], self.ycor() + TAIL_CENTER[1]
