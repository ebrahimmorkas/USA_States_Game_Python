# The coordinates of the states according to the image that will be displayed when we run the file is done nd to know how to remove the coordinates of the states according to the screen then see the video 230 in it, it is explained
import turtle as tur
import pandas
turtle = tur.Turtle()
screen = tur.Screen()
screen.title("Game")
screen .addshape("blank_states_img.gif")
tur.shape("blank_states_img.gif")

# Reading the csv file of states
data = pandas.read_csv("50_states.csv")
# print(data)
list_of_states_name = data["state"]
# We have to create ths new list because the data in the previous list is in the form of csv format so it wont work much
new_list_of_states = []
for i in range(0, len(list_of_states_name)):
    new_list_of_states.append(list_of_states_name[i])
list_of_x_coordinate = data["x"]
list_of_y_coordinate = data["y"]

# variable that will toggle that how many states has been entered by the user
states_toggler = 0

# variable that will check whether all the 50 states has been entered by the user or not and if user has entered all the 50 states then with the help if this variable we will exit the while loop
while_loop_toggler = True

# Creating the list that will hold all states names that is entered by the user so this list will help us to prevent the redundancy that is  it will protect user by entering the same name multiple times
states_entered_by_user = []

while while_loop_toggler:
    if states_toggler == 2:
        while_loop_toggler = False
    user_input = screen.textinput("STATES", "Enter the USA state")
    if user_input in new_list_of_states:
        if user_input not in states_entered_by_user:
            print(user_input)
            states_toggler += 1
            states_entered_by_user.append(user_input)
            turtle.penup()
            turtle.goto(-203, -40)
            turtle.pendown()
            turtle.write(user_input, align="left", font=("Arial", 12, "normal"))
    else:
        print("Not present")
screen.exitonclick()