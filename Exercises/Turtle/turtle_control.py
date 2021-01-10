from turtle import Turtle, Screen

stas = Turtle()
screen = Screen()


def move_forwards():
    stas.forward(10)
def move_backwards():
    stas.back(10)
def turn_left():
    stas.left(5)
def turn_right():
    stas.right(5)
def clear_screen():
    stas.speed(0)
    stas.penup()
    stas.clear()
    stas.home()
    stas.speed(6)
    stas.pendown()

screen.listen()
screen.onkeypress(key='w', fun=move_forwards)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='c', fun=clear_screen)


screen.exitonclick()