from turtle import Turtle


class Bullet(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.hideturtle()

    def shoot(self, x, y):
        self.goto(x, y)
        self.showturtle()

    def move(self):
        self.sety(self.ycor() + 15)

    def reset(self):
        self.hideturtle()
        self.goto(0, -1000)
