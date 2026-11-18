"""This is a python program to draw hirst painting with turtle and random imports.
This also uses the colorgram import found in the utils.py initially
to extract all the Hirst Dot Painting's color palette based on the jpg."""
from turtle import Turtle,Screen
import random

turtle = Turtle()
screen = Screen()
turtle.penup()
turtle.hideturtle()
screen.colormode(255)
color_list = [(158, 21, 46), (231, 206, 80), (40, 95, 160), (227, 72, 44), (218, 146, 78), (218, 76, 115), (106, 173, 216), (66, 46, 29), (63, 121, 53), (175, 84, 37), (124, 197, 143), (21, 37, 86), (33, 61, 38), (133, 212, 197), (127, 113, 190), (200, 136, 156)]
current_y = -200
# The painting should be 10 x 10
for row in range (10):
    current_y +=50
    turtle.goto(-400,current_y)
    print(turtle.position())
    for col in range (19):
        turtle.dot(25, random.choice(color_list))
        if col % 2 == 0:
            turtle.penup()
            # Each dot should have 50 paces in between.
            turtle.forward(50)

screen.exitonclick()