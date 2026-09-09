import pandas
import turtle
from turtle import Screen

data = pandas.read_csv("day-25-us-states-game-start/50-states.csv")
all_states = data.state.to_list()
guessed_state = []

screen = Screen()
screen.title("U.S. States Game")
image = "day-25-us-states-game-start/blank-states-img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0

while len(guessed_state) < 50:
    answer_state = screen.textinput(title = f"{score}/50 states are correct", prompt = "Enter name of the State").title()
    
    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_state:
                missed_states.append(state)
        print(missed_states)
        missed_data = pandas.DataFrame(missed_states)
        missed_data.to_csv("missed_states.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        score += 1
        turbo = turtle.Turtle()
        turbo.hideturtle()
        turbo.penup()
        state_info = data[data.state == answer_state]
        turbo.goto(state_info.x.item(),state_info.y.item())
        turbo.write(state_info.state.item())
    







