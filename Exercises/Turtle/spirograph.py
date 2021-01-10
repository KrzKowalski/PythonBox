import turtle as t
import random

t.colormode(255)
screen = t.Screen()
screen.screensize(1000, 800)

stas = t.Turtle()
stas.shape('arrow')
stas.speed(0)


def pick_random_color():
    random_red = random.randint(1, 255)
    random_green = random.randint(1, 255)
    random_blue = random.randint(1, 255)
    color = (random_red, random_green, random_blue)
    return color


def circle_spirograph(turtle_obj, radius, density):
    x = density
    for _ in range (int(360/density)):
        turtle_obj.color(pick_random_color())
        turtle_obj.circle(radius=radius)
        # turtle_obj.setheading(turtle_obj.heading() + density)
        turtle_obj.setpos(x,x)
        x+=density
turtle = t.Turtle()



circle_spirograph(stas, 120, 4)
screen.exitonclick()