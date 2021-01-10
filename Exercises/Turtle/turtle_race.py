from turtle import Turtle, Screen
import random

race_start = False
screen = Screen()
#SETUP:
set_width = 1500
set_height = 600
max_speed = 20

screen.setup(width=set_width, height=set_height)
screen.canvheight = set_height
screen.bgcolor('silver')
user_bet = screen.textinput(title="Make a bet!", prompt="Who will win the race? Enter a color: ").lower()
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
    race_start = True

while race_start:
    for turtle in all_turtles:
        if turtle.xcor() > int(set_width/2-20):
            race_start = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost... The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, max_speed)
        turtle.forward(rand_distance)


screen.exitonclick()