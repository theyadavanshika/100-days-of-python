from turtle import Screen, Turtle
from enemy import Enemy
from bullet import Bullet
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

screen.register_shape("images/alien1.gif")
screen.register_shape("images/alien2.gif")
screen.register_shape("images/alien3.gif")


game_is_running = True
enemy_speed = 5
direction = 1

enemies = []
bullets = []


player = Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -250)
player.setheading(90)
player.shapesize(stretch_wid=2, stretch_len=2)

scoreboard = Scoreboard()


def move_left():
    if not game_is_running:
        return

    if player.xcor() > -360:
        player.setx(player.xcor() - 20)


def move_right():
    if not game_is_running:
        return

    if player.xcor() < 360:
        player.setx(player.xcor() + 20)


def shoot():
    if not game_is_running:
        return

    bullet = Bullet()
    bullet.shoot(player.xcor(), player.ycor())
    bullets.append(bullet)


alien_types = [
    ("images/alien1.gif", 30),
    ("images/alien2.gif", 20),
    ("images/alien3.gif", 10),
]


def create_enemies():
    for row in range(3):
        shape, points = alien_types[row]

        for col in range(5):
            enemy = Enemy(shape, points)

            x = -250 + (col * 100)
            y = 200 - (row * 70)

            enemy.goto(x, y)
            enemies.append(enemy)


def move_enemies():
    global direction, game_is_running

    if not game_is_running:
        return

    for enemy in enemies:
        enemy.move(enemy_speed * direction)

    if any(enemy.xcor() > 360 for enemy in enemies):
        direction = -1

        for enemy in enemies:
            enemy.move_down()

    elif any(enemy.xcor() < -360 for enemy in enemies):
        direction = 1

        for enemy in enemies:
            enemy.move_down()

    for enemy in enemies:
        if enemy.distance(player) < 40:
            scoreboard.lose_life()
            enemy.hideturtle()
            enemies.remove(enemy)

            if scoreboard.lives == 0:
                game_is_running = False
                scoreboard.game_over()
                screen.update()
                return

            break

    screen.update()
    screen.ontimer(move_enemies, 20)


def move_bullets():
    global game_is_running

    if not game_is_running:
        return

    for bullet in bullets[:]:
        bullet.move()

        for enemy in enemies:
            if bullet.distance(enemy) < 25:

                enemy.hideturtle()
                enemies.remove(enemy)

                bullet.hideturtle()
                bullets.remove(bullet)

                scoreboard.score += enemy.points
                scoreboard.update_score()

                if len(enemies) == 0:
                    game_is_running = False
                    scoreboard.you_win()
                    screen.update()
                    return

                break

        if bullet in bullets and bullet.ycor() > 300:
            bullet.hideturtle()
            bullets.remove(bullet)

    screen.update()
    screen.ontimer(move_bullets, 20)


def game_loop():
    if game_is_running:
        screen.update()
        screen.ontimer(game_loop, 20)


def restart_game():
    global game_is_running, enemy_speed, direction

    if game_is_running:
        return

    game_is_running = True
    enemy_speed = 5
    direction = 1

    player.goto(0, -250)
    player.setheading(90)
    player.showturtle()

    scoreboard.score = 0
    scoreboard.lives = 3
    scoreboard.goto(-100, 260)
    scoreboard.update_score()

    for enemy in enemies:
        enemy.hideturtle()

    enemies.clear()

    for bullet in bullets:
        bullet.hideturtle()

    bullets.clear()

    create_enemies()

    screen.update()

    move_enemies()
    move_bullets()
    game_loop()


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(shoot, "space")
screen.onkeypress(restart_game, "r")
screen.onkeypress(restart_game, "R")


create_enemies()

move_enemies()
move_bullets()
game_loop()

screen.exitonclick()
