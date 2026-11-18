""" Inspired by etch-a-sketch classic game where this is to learn about higher order functions and event listeners
Modules:
    - Turtle
    - Screen
"""
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def turn_left():
    turtle.left(5)

def turn_right():
    turtle.right(10)

def clear_drawing():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=turn_left)
screen.onkey(key="D", fun=turn_right)
screen.onkey(key="C", fun=clear_drawing)


screen.exitonclick()