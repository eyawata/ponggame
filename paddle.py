from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(xcor, ycor)

    def right_go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def right_go_down(self):
        if self.ycor() > -225:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def left_go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def left_go_down(self):
        if self.ycor() > -225:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

