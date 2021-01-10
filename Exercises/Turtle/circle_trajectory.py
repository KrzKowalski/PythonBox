import turtle as t
import random

t.colormode(255)
screen = t.Screen()
screen.screensize(1000, 800)
def pick_random_color():
    random_red = random.randint(1, 255)
    random_green = random.randint(1, 255)
    random_blue = random.randint(1, 255)
    color = (random_red, random_green, random_blue)
    return color

def draw_shape(number_of_sides, turtle_name):
    color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    turtle_name.pencolor(color)
    for _ in range(number_of_sides):
        turtle_name.forward(100)
        turtle_name.right(360 / number_of_sides)

stas = t.Turtle()
stas.shape('arrow')
stas.speed(9)


def draw_donut(R_radius, r_radius, density):
    for i in range(1, 360, density):
        stas.color(pick_random_color())
        stas.penup()
        stas.circle(R_radius, i)
        stas.right(90)
        stas.forward(50)
        stas.left(90)
        stas.pendown()
        # draw_shape(15, stas) ##optional other shape
        stas.circle(r_radius)
        stas.penup()
        stas.home()


draw_donut(100, 50, 60)

screen.exitonclick()