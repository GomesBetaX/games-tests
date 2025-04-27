import turtle
import pandas
import scores
import writer

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)

sc = scores.Scoreboard()
write = writer.Writer()

# file path to image
IMAGE_PATH = "./us_game/blank_states_img.gif"

# add image to screen
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

data = pandas.read_csv("./us_game/50_states.csv")

# guess states
guessed_states = []
total_states = data[data.columns[0]].count()
states_list = data["state"]

# show latest highscore
turtle.textinput(title=f"Your highscore is: {sc.get_highschore()}", prompt="Press enter to start the game!")

# Lopp until game on is false
game_on = True
while game_on:
    answer = turtle.textinput(title="Guess the State", prompt="Guess:")
    answer = answer.capitalize()

    if answer in guessed_states:
        print("Already guessed.")
        continue

    if answer not in states_list.values:
        print("Not a state")
    else:
        guessed_state = data[data["state"] == answer]
        sc.update_score()
        sc.write_score()
        x = guessed_state.x.item()
        y = guessed_state.y.item()
        write.write_state(answer, x, y)
        guessed_states.append(answer)

    if answer.lower() == "exit":
        game_on = False
        screen.bye()


# get user coordinates
# def get_mouse_click_coor(x,y):
#    print(x, y)
#    # get column and row of state
#    print(data[data.state == "Alabama"])
# screen.onscreenclick(get_mouse_click_coor)

# closes screen when window is closed
screen.mainloop()