import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

loop_counter = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    #Only creates the car when the loop_counter is greater than 6
    loop_counter += 1
    if loop_counter > 6:
        loop_counter = 0
        car_manager.create_car()
    car_manager.move_cars()

    #Detects collision with the car
    for car in car_manager.car_list:
        if car.distance(player) < 25:
            #it is game over
            score_board.game_over()
            game_is_on = False

    #Check if the turtle is on the tip of the y_axis:
    if player.is_finish_line():
        score_board.update_level()
        car_manager.increase_speed()
        player.restart_player()


screen.exitonclick()


