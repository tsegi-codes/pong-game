from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))

ball = Ball((0,0))

l_board = ScoreBoard((-50, 250))
r_board = ScoreBoard((50, 250))



screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w".lower())
screen.onkeypress(l_paddle.move_down, "s".lower())



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 65 and ball.xcor() > 320 or ball.distance(l_paddle) < 65 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_ball()
        ball.bounce_x()
        l_board.increase_score()
    if ball.xcor() < -380:
        ball.reset_ball()
        ball.bounce_x()
        r_board.increase_score()


    if r_board.score > 10 or l_board.score > 10:
        game_is_on = False







screen.exitonclick()