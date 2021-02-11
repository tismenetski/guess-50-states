import turtle
from state import State
import pandas

# Screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



#Data from csv
data = pandas.read_csv("50_states.csv").to_dict()

#Local variables to keep track of result
num_of_states = len(data["state"])
correct_guesses = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt=f"Guessed: {correct_guesses}/{num_of_states}\nWhat's another state name?")
    answer  = answer_state.title() # Convert each input to uppercase , new york = New York

    if answer == "Exit":
        break
    #print(answer)
    for state in data["state"].items():
        if answer==state[1] and answer not in guessed_states:
            correct_guesses+=1
            guessed_states.append(answer)
            key = state[0]
            xcor = data['x'][key]
            ycor = data['y'][key]
            new_state = State()
            new_state.name_state(answer)
            new_state.move_state(xcor,ycor)




# def get_mouse_click_coor(x,y):
#     print(x,y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)



#print(answer_state)


not_guessed_states = []
for state in data["state"].items():
    print(state)
    if state[1] not in guessed_states:
        not_guessed_states.append(state[1])


data_output = pandas.DataFrame(not_guessed_states)
data_output.to_csv("not_guessed_states.csv")





#  screen.exitonclick()



#def get_coordinates(name):
