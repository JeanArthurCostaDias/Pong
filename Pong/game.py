from main import Players, turtles
from turtle import Screen
from score import Scoreboard
from ball import Ball

is_on = True
sticks = Players()
screen = Screen()
scoreboard = Scoreboard()
screen.title("pong")
screen.bgcolor("black")
screen.setup(800,600)
ball = Ball()
while is_on:
    screen.update()
    sticks.bot_movement()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(turtles[0]) < 70 and ball.xcor() > 370 or ball.distance(turtles[1]) < 90 and ball.xcor() > -370:
        ball.bounce_x()
    if ball.xcor() > 380:
        scoreboard.new_score_bot()
        ball.reset_ball()
    elif ball.xcor() < -380:
        scoreboard.new_score_player()
        ball.reset_ball()

screen.exitonclick()