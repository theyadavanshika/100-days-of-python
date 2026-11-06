from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3

        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)

        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "bold"))

        self.goto(250, 260)
        self.write(f"Lives: {self.lives}", align="center", font=("Arial", 18, "bold"))

    def increase_score(self):
        self.score += 10
        self.update_score()

    def lose_life(self):
        self.lives -= 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
        self.restart_message()

    def you_win(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Arial", 30, "bold"))
        self.restart_message()

    def restart_message(self):
        self.goto(0, -50)
        self.write("Press R to Restart", align="center", font=("Arial", 18, "bold"))
