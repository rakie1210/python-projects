from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
map_answer = Turtle()
turtle.shape(image)
score = 0
guessed_state_list = list()

df = pd.read_csv("50_states.csv")
while score < 50:
    if score == 0:
        answer_state = str(screen.textinput(title="Guess the state", prompt="What's another state's name?")).title()
    else:
        answer_state = str(screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")).title()

    state_info = df[df["state"] == answer_state]
    #State is found
    if not state_info.empty:
        x_cord = state_info["x"].item()
        y_cord = state_info["y"].item()
        map_answer.penup()
        map_answer.hideturtle()
        map_answer.goto(x_cord, y_cord)
        map_answer.write(answer_state, align="center" ,font=("Arial", 10, "normal"))
        guessed_state_list.append(answer_state)
        score += 1
    if answer_state == "Exit":
        missing_values = set(df["state"].tolist()) - set(guessed_state_list)
        data = pd.DataFrame(missing_values).sort_values(by=0, ascending=True)
        data.to_csv("states_to_learn.csv")
        break

#For getting the x and y coordinates of the map
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()
screen.exitonclick()