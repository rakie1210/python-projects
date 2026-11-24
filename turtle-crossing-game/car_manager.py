""" A class that creates the cars in the game"""
from turtle import Turtle, Screen, Shape
import math
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
WINDOW_COLOR = "light sky blue"
WHEEL_COLOR = "black"


def _to_shape_coords(points):
    """Convert screen offsets (dx, dy) into turtle shape coordinates.

    Cars face left (heading 180). For that heading, turtle draws a shape
    point (x, y) at screen offset (-y, x), so we invert that here.
    """
    return tuple((dy, -dx) for dx, dy in points)


def _circle(center_x, center_y, radius, sides=10):
    return [(center_x + radius * math.cos(2 * math.pi * i / sides),
             center_y + radius * math.sin(2 * math.pi * i / sides))
            for i in range(sides)]


def _register_car_shapes():
    """Register one car-shaped compound shape per color, e.g. 'car_red'.

    The car is drawn facing left (its direction of travel), about 40px long.
    """
    body = [(-20, -4), (-20, 3), (-16, 6), (16, 6), (20, 3), (20, -4)]
    cabin = [(-8, 6), (-3, 14), (10, 14), (13, 6)]
    front_window = [(-6, 7), (-2, 12), (3, 12), (3, 7)]
    back_window = [(5, 7), (5, 12), (9, 12), (11, 7)]
    front_wheel = _circle(-11, -5, 4)
    back_wheel = _circle(11, -5, 4)

    screen = Screen()
    for color in COLORS:
        car_shape = Shape("compound")
        car_shape.addcomponent(_to_shape_coords(body), color, "black")
        car_shape.addcomponent(_to_shape_coords(cabin), color, "black")
        car_shape.addcomponent(_to_shape_coords(front_window), WINDOW_COLOR)
        car_shape.addcomponent(_to_shape_coords(back_window), WINDOW_COLOR)
        car_shape.addcomponent(_to_shape_coords(front_wheel), WHEEL_COLOR)
        car_shape.addcomponent(_to_shape_coords(back_wheel), WHEEL_COLOR)
        screen.register_shape(f"car_{color}", car_shape)


class CarManager (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.y_position = random.randint(-300, 300)
        self.penup()
        self.car_list= []
        self.move_speed = STARTING_MOVE_DISTANCE
        _register_car_shapes()


    def create_car(self):
        new_car = Turtle(shape=f"car_{random.choice(COLORS)}")
        new_car.setheading(180)
        new_y_position = random.randint(-250, 250)
        new_car.penup()
        new_car.goto(300, new_y_position)
        self.car_list.append(new_car)


    #Let the rectangle move from right to left
    def move_cars(self):
        for car in self.car_list:
            car.penup()
            car.setheading(180)
            car.forward(self.move_speed)

    def increase_speed(self):
        # Level 1 = 5, level 2 = 8, level 3 = 11, ... applies to every car
        self.move_speed += MOVE_INCREMENT






