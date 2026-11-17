import random

def drawingdifferentshape(tim,total_sides,total_angle):
    """Drawing triangle to decagon using the turtle graphics"""
    colors = ["firebrick","DarkOrange","gold1","green4","DodgerBlue","DarkOrchid4","orchid","purple4"]
    for shape in range(0,len(total_sides)):
        shape_angle = total_angle/total_sides[shape]
        tim.color(colors[shape])
        tim.pendown()
        for side in range(total_sides[shape]):
            print(side)
            tim.forward(100)
            tim.right(shape_angle)
        tim.penup()

def random_color():
    """Creating a rgb colors randomly"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

def randomwalk(tim,steps, direction):
    """Making the turtle do a random walk
    Parameters:
        tim as the Turtle object
        steps as the number of iterations
        direction as the direction of the turtle
    """
    tim.pensize(8)

    tim.pendown()

    for i in range(steps):
        tim.color(random_color())
        tim.forward(50)
        tim.setheading(random.choice(direction))

def spirograph(tim,radius,size_of_gap):
    """Making the turtle do a spirograph
    Parameters:
        tim as the Turtle object
        radius as the radius of the circle
        size_of_gap as the size of the gap of the circles
    """
    tim.pendown()
    tim.speed("fastest")
    for i in range(360//size_of_gap):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading()+size_of_gap)







