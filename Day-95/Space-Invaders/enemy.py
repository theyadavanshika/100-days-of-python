from turtle import Turtle


class Enemy(Turtle):
    def __init__(self, alien_shape, points):
        super().__init__()

        self.shape(alien_shape)
        self.points = points
        self.penup()

    def move(self, distance):
        new_x = self.xcor() + distance
        self.setx(new_x)

    def move_down(self):
        self.sety(self.ycor() - 20)
