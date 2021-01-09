from turtle import Turtle, Screen
import random


def draw_shape(number_of_sides, turtle_name):
    color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    turtle_name.pencolor(color)
    for _ in range(number_of_sides):
        turtle_name.forward(100)
        turtle_name.right(360 / number_of_sides)


screen = Screen()
screen.colormode(255)
screen.screensize(canvwidth=200, canvheight=200, bg='black')

zuf = Turtle()
zuf.shape('turtle')
zuf.color("black", "dark khaki")

sides = 3
while sides <= 10:
    draw_shape(sides, zuf)
    sides += 1
    
screen.exitonclick()

