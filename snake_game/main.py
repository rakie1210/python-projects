from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Snake game screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

#Listen to arrow keystrokes
screen.listen()
screen.onkey(snake.up,key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left,key="Left")
screen.onkey(snake.right,key="Right")

game_is_on = True
while game_is_on:
    #Refreshes the screen
    screen.update()
    time.sleep(0.1)
    #Moves forward
    snake.move()

    #Detect collision with food (the mouse's body or its tail).
    if snake.head.distance(food) < 15 or snake.head.distance(food.tail_position()) < 10:
        #Increase the score to 1
        score.increase_score()
        snake.extend_segment()
        food.refresh()

    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        #Shows game over and the final score.
        score.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            #Trigger game over.
            game_is_on = False
            score.game_over()


screen.exitonclick()



