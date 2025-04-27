import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)

# file path to image
IMAGE_PATH = "./us_game/blank_states_img.gif"

# add image to screen
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

data = pandas.read_csv("./us_game/50_states.csv")

def get_mouse_click_coor(x,y):
   print(x,y)
screen.onscreenclick(get_mouse_click_coor)

# closes screen when window is closed
screen.mainloop()