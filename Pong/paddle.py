from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position_tuple):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setpos(position_tuple)
        self.setheading(0)

    def move_up(self):
        new_pos = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_pos)

    def move_down(self):
        new_pos = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_pos)
