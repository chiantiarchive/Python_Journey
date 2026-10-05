

import turtle
import random

# ----------------------------
# WINDOW SETUP
# ----------------------------
screen = turtle.Screen()
screen.title("Turtle Space Shooter")
screen.bgcolor("black")
screen.setup(width=800, height=700)
screen.tracer(0)

WIDTH = 800
HEIGHT = 700
LEFT_EDGE = -WIDTH // 2
RIGHT_EDGE = WIDTH // 2
TOP_EDGE = HEIGHT // 2
BOTTOM_EDGE = -HEIGHT // 2

# ----------------------------
# GAME SETTINGS
# ----------------------------
PLAYER_SPEED = 18
BULLET_SPEED = 15
ENEMY_SPEED = 3
ENEMY_SPAWN_EVERY = 35
MAX_ENEMIES = 12

score = 0
game_over = False
frame_count = 0

bullets = []
enemies = []

# ----------------------------
# TEXT
# ----------------------------
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.color("white")
score_writer.penup()
score_writer.goto(-380, 300)


def show_score():
    score_writer.clear()
    score_writer.write(
        f"Score: {score}",
        align="left",
        font=("Arial", 18, "bold")
    )


message_writer = turtle.Turtle()
message_writer.hideturtle()
message_writer.color("white")
message_writer.penup()

# ----------------------------
# PLAYER SHIP
# ----------------------------
player = turtle.Turtle()
player.shape("triangle")
player.color("#34eb83")
player.penup()
player.setheading(90)
player.goto(0, -280)


# ----------------------------
# CONTROLS
# ----------------------------
def move_left():
    if not game_over:
        new_x = player.xcor() - PLAYER_SPEED

        if new_x > LEFT_EDGE + 25:
            player.setx(new_x)


def move_right():
    if not game_over:
        new_x = player.xcor() + PLAYER_SPEED

        if new_x < RIGHT_EDGE - 25:
            player.setx(new_x)


def shoot():
    if game_over:
        return

    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.color("#00e5ff")
    bullet.shapesize(stretch_wid=0.25, stretch_len=0.8)
    bullet.penup()
    bullet.goto(player.xcor(), player.ycor() + 22)

    bullets.append(bullet)


# ----------------------------
# CREATE ENEMIES
# ----------------------------
def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("#ff3b3b")
    enemy.shapesize(stretch_wid=1.1, stretch_len=1.1)
    enemy.penup()

    x = random.randint(LEFT_EDGE + 30, RIGHT_EDGE - 30)
    y = TOP_EDGE - 35

    enemy.goto(x, y)
    enemies.append(enemy)


# ----------------------------
# COLLISION CHECK
# ----------------------------
def touching(object_a, object_b, distance=22):
    return object_a.distance(object_b) < distance


# ----------------------------
# END GAME
# ----------------------------
def end_game():
    global game_over
    game_over = True

    message_writer.goto(0, 20)
    message_writer.write(
        "GAME OVER",
        align="center",
        font=("Arial", 32, "bold")
    )

    message_writer.goto(0, -30)
    message_writer.write(
        f"Final score: {score}\nPress R to restart",
        align="center",
        font=("Arial", 18, "normal")
    )


# ----------------------------
# RESTART GAME
# ----------------------------
def restart():
    global score, game_over, frame_count

    if not game_over:
        return

    # Remove old bullets
    for bullet in bullets:
        bullet.hideturtle()
    bullets.clear()

    # Remove old enemies
    for enemy in enemies:
        enemy.hideturtle()
    enemies.clear()

    score = 0
    frame_count = 0
    game_over = False

    player.goto(0, -280)
    message_writer.clear()
    show_score()


# ----------------------------
# MAIN GAME LOOP
# ----------------------------
def game_loop():
    global score, frame_count

    if not game_over:
        frame_count += 1

        # Add an enemy every so often
        if frame_count % ENEMY_SPAWN_EVERY == 0 and len(enemies) < MAX_ENEMIES:
            create_enemy()

        # Move bullets upward
        for bullet in bullets[:]:
            bullet.sety(bullet.ycor() + BULLET_SPEED)

            # Delete bullets that leave the screen
            if bullet.ycor() > TOP_EDGE + 20:
                bullet.hideturtle()
                bullets.remove(bullet)

        # Move enemies downward
        for enemy in enemies[:]:
            enemy.sety(enemy.ycor() - ENEMY_SPEED)

            # Enemy reaches bottom: game over
            if enemy.ycor() < BOTTOM_EDGE - 10:
                end_game()
                break

            # Enemy hits player
            if touching(enemy, player, 28):
                end_game()
                break

            # Bullet hits enemy
            for bullet in bullets[:]:
                if touching(bullet, enemy, 23):
                    bullet.hideturtle()
                    enemy.hideturtle()

                    bullets.remove(bullet)
                    enemies.remove(enemy)

                    score += 1
                    show_score()
                    break

    screen.update()
    screen.ontimer(game_loop, 20)


# ----------------------------
# KEY BINDINGS
# ----------------------------
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(shoot, "space")
screen.onkeypress(restart, "r")
screen.onkeypress(restart, "R")

show_score()
game_loop()
turtle.done()