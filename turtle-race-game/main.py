""" A simple game of Turtle Race Game where six turtles start in a column
 and move random distances until one crosses the finish line.
 The user's bet is compared to the winning turtle's color. """

from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the rase? Enter a color: ")
is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = list()
y_axis = -100


for turtle_indx in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_indx])
    new_turtle.penup()
    y_axis += 30
    new_turtle.goto(x=-230,y=y_axis)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win! {winning_turtle} turtle is the winner!")
            else:
                print(f"You lose! {winning_turtle} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()