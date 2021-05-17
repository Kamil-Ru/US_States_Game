import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

imported_csv_file = pandas.read_csv("50_states.csv")
print(imported_csv_file)
state_list = imported_csv_file["state"].to_list()


points = 0
state_list_answer = []
game_is_on = True
while game_is_on:
    screen.update()

    if points == 50:
        end_game = screen.textinput(title=f"New game?", prompt="You guessed all state. Type 'n' for new game, or 'q' "
                                                               "for quit")
        if end_game == "q":
            break
        elif end_game == "n":
            points = 49
            state_list_answer = []
            game_is_on = True

    answer_state = (screen.textinput(title=f"{points} / 50 states", prompt="What's another state's name?")).title()

    if answer_state == "Q":
        state_list = pandas.DataFrame(state_list)
        state_list.to_csv("Missing_states.csv")
        break

    if answer_state in state_list and answer_state not in state_list_answer:
        state_list.remove(answer_state)
        state_list_answer.append(answer_state)
        points += 1
        x_cor = int(imported_csv_file[imported_csv_file.state == answer_state].x)
        y_cor = int(imported_csv_file[imported_csv_file.state == answer_state].y)
        naw_state_object = State(x_cor, y_cor, answer_state)
        print(state_list_answer)


