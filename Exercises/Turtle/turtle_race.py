from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
#SETUP:
set_width = 800
set_height = 600
max_speed = 20

screen.setup(width=set_width, height=set_height)
screen.canvheight = set_height
screen.bgcolor('silver')
user_bet = screen.textinput(title="Make a bet!", prompt="Who will win the race? Enter a color:\n"
                                                        "['red', 'orange', 'yellow', 'green', 'blue', 'purple', "
                                                        "'white', 'black', 'brown']").lower()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white', 'black', 'brown']
t_position = screen.canvheight / len(colors)
all_turtles = []

for turtle_index in range(0, len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color("black", colors[turtle_index])
    new_turtle.goto(x=int(((set_width/2)*-1)+20), y=int(((set_height/2)*-1)+30) + turtle_index * t_position)
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True
score_list = []
while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() >= int(set_width/2-20):
            # race_start = False
            at_finish_color = turtle.fillcolor()
            if at_finish_color not in score_list:
                score_list.append(at_finish_color)
        rand_distance = random.randint(0, max_speed)
        turtle.forward(rand_distance)

    if len(score_list) == len(all_turtles):
        race_is_on = False
        place = 0
        print("THE FINAL RESULTS:")
        for score in score_list:
            place += 1
            if score == user_bet:
                print(f"{place}. {score} turtle <--- USER BET")
            else:
                print(f"{place}. {score} turtle")


screen.exitonclick()