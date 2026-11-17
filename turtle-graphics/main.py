import turtle
from turtle import Turtle, Screen
import turtlechallenge

tim = Turtle()
turtle.colormode(255)
screen = Screen()
tim.penup()
tim.goto(200, -200)
# Triangle, Square,Pentagon, Hexagon, Heptagon, Octagon, Nonagon, Decagon
# shapes_sides = [3,4,5,6,7,8,9,10]
# ANGLE = 360
# turtlechallenge.drawingDifferentShape(tim,shapes_sides,ANGLE)

# STEPS = 200
# directions =[0,90,180,270]
# turtlechallenge.randomwalk(tim, STEPS, directions)

#turtlechallenge.spirograph(tim,100,2)

screen.exitonclick()
