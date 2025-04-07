from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
game_is_on = True
SLEEP = 0.1

# Screen setup
screen = Screen()
screen.screensize(SCREEN_WIDTH,SCREEN_HEIGHT)
screen.setup(SCREEN_WIDTH+350, SCREEN_HEIGHT+50)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Position a turle in the bottom of the screen, preping it
middle_line = Turtle()
middle_line.penup()
middle_line.goto(0,-380)
middle_line.color("white")
middle_line.pensize(5)
middle_line.speed("fastest")
middle_line.hideturtle()

# make a loop of the turtle to walk up with pen down - pen up alternating
for y in range(-SCREEN_HEIGHT,SCREEN_HEIGHT,20):
    if y%40 == 20:
        middle_line.penup()
        middle_line.goto(0, y)
    else:
        middle_line.pendown()
        middle_line.goto(0, y)
        

# Setup left paddle
r_paddle = Paddle((500,0))
l_paddle = Paddle((-500,0))

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



ball = Ball()
# Define scorepositions
l_score = Scoreboard((-50,200))
r_score = Scoreboard((50,200))

screen.update()

#ball.move()

while game_is_on:
    screen.update()
    time.sleep(SLEEP)
    ball.move()


    # If ball hits top or bottom wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()


    # If ball hits paddle
    if ball.xcor()>470 and ball.distance(r_paddle) < 50 or ball.xcor()<-470 and ball.distance(l_paddle) < 50:
        ball.hit()
        SLEEP = SLEEP/1.4
   # Right paddle misses
    elif ball.xcor() > 550 and ball.distance(r_paddle) > 50:
        l_score.scored_point()
        ball.reset_ball()
        SLEEP = 0.1
        screen.update()
    # Left paddle misses
    elif ball.xcor() < -550 and ball.distance(l_paddle) > 50:
        r_score.scored_point()
        ball.reset_ball()
        screen.update()
        SLEEP = 0.1



screen.exitonclick()

