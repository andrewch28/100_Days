import turtle
import pandas as pd
from states import States
state = States()

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df['state'].to_list()


guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        correct_state = df[df['state'] == answer_state]
        choice = correct_state['state'].item()
        x = correct_state['x'].item()
        y = correct_state['y'].item()
        state.print_state(choice, x, y)

for i in guessed_states:
    if i in all_states:
        all_states.remove(i)

df_new = pd.DataFrame(all_states)
df_new.to_csv("states_to_learn.csv")