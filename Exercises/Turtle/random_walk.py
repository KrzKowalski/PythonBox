from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
screen.screensize(1000, 800)

stas = Turtle()
stas.shape('blank')
stas.pensize(5)

def random_turtle_walk(turtle_obj, number_of_steps, speed=6):
    """
    The function simulates the random walk
    :param turtle_obj: an instance of a Turtle() class
    :param number_of_steps: number of steps done by a turtle
    :param speed: default = 6, speed of a random walk higher integer means higher speed
    """
    directions = [90, 180, 270, 360]
    turtle_obj.speed(speed)
    for i in range(number_of_steps):
        turtle_obj.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        turtle_obj.forward(15)
        # turtle_obj.seth(random.choice(directions))
        turtle_obj.seth(random.randint(0 ,360))


random_turtle_walk(stas, 1000, 50)


screen.exitonclick()