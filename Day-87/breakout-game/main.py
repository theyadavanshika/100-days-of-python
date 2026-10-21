import turtle
from turtle import Screen, Turtle

screen = turtle.Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Breakout Game")

x_move = 10
y_move = 10

score = 0


def move_ball():
    global x_move, y_move, score

    if ball.xcor() > 380 or ball.xcor() < -380:
        x_move *= -1

    if ball.ycor() > 280:
        y_move *= -1

    if y_move < 0 and -240 < ball.ycor() < -220:
        if abs(ball.xcor() - paddle.xcor()) < 60:
            y_move *= -1

    if ball.ycor() < -290:
        game_over_display = Turtle()
        game_over_display.color("white")
        game_over_display.penup()
        game_over_display.hideturtle()
        game_over_display.goto(0, 0)
        game_over_display.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        return

    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.hideturtle()
            bricks.remove(brick)

            score += 10
            score_display.clear()
            score_display.write(
                f"Score: {score}", align="left", font=("Arial", 16, "normal")
            )

            y_move *= -1
            break

    if len(bricks) == 0:
        win_display = Turtle()
        win_display.color("white")
        win_display.penup()
        win_display.hideturtle()
        win_display.goto(0, 0)
        win_display.write("YOU WIN!", align="center", font=("Arial", 24, "bold"))
        return

    current_xpos = ball.xcor() + x_move
    current_ypos = ball.ycor() + y_move
    ball.goto(current_xpos, current_ypos)

    screen.ontimer(move_ball, 30)


def move_left():
    current_pos = paddle.xcor()
    next_pos = max(current_pos - 20, -350)
    paddle.goto(x=next_pos, y=-250)


def move_right():
    current_pos = paddle.xcor()
    next_pos = min(current_pos + 20, 350)
    paddle.goto(x=next_pos, y=-250)


paddle = Turtle()
paddle.shape("square")
paddle.color("deepskyblue")
paddle.penup()
paddle.goto(x=0, y=-250)
paddle.shapesize(stretch_wid=0.4, stretch_len=5)

bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
screen.tracer(0)

for row in range(5):
    for col in range(10):
        brick = Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.penup()
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.goto(x=-350 + col * 70, y=220 - row * 30)
        bricks.append(brick)

screen.update()
screen.tracer(1)

score_display = Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-350, 260)
score_display.write("Score: 0", align="left", font=("Arial", 16, "normal"))

ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(x=0, y=-230)

screen.listen()
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")

move_ball()
screen.exitonclick()
