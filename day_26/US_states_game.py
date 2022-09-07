import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = './day_26/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('./day_26/50_states.csv')
# all_states = data.state.to_list()


guessed = []
cnt = 0
continue_game = True
while continue_game == True:
    stored_answers = len(guessed)
    answer_state = screen.textinput(title=f'{stored_answers}/50 States Correct', prompt="What's another state's name?")
    answer_state.title()

    if answer_state == 'Exit':
        # missed = []
        # for s in data.state.to_list():
        #     if s not in guessed:
        #         missed.append(s)
        missed = [s for s in data.state.to_list() if s not in guessed]


        print("The states you missed.")
        print("-----------------------")
        print(f"{missed}\n")

        saved = pandas.DataFrame(missed)
        saved.to_clipboard("./day_26/states_to_learn.csv")

        continue_game == False
        quit()

    

    if answer_state in data.state.to_list():
        guessed.append(answer_state)
        pin = turtle.Turtle()
        pin.hideturtle()
        pin.penup()
        coordinate = data[data.state == answer_state]
        pin.goto(int(coordinate.x), int(coordinate.y))
        pin.write(answer_state,font=('Corient', 8, 'normal'))
        if cnt == 50:
            pin.write("Congradulations!\nYou know all the states!")
            continue_game = False