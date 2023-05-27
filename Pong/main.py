from turtle import Turtle,Screen

turtles = []
screen = Screen()


class Players:
    def __init__(self):
        tim = Turtle(shape="square")
        tim.shapesize(stretch_wid=5, stretch_len=0.5)
        tim.color("white")
        tim.penup()
        self.new_y = 10
        tim.goto(380, 0)
        turtles.append(tim)
        self.create_stick()
        self.stick_movement()

    def create_stick(self):
        tim = Turtle()
        tim.shape("square")
        tim.shapesize(stretch_wid=5, stretch_len=0.5)
        tim.color("white")
        tim.penup()
        tim.goto(-380, 0)
        turtles.append(tim)

    def stick_movement(self):
        screen.listen()
        screen.onkeypress(self.move_up,"w")
        screen.onkeypress(self.move_down, "s")

    def move_up(self):
        xcor = turtles[0].xcor()
        ycor = turtles[0].ycor()
        if ycor < 240:
            turtles[0].goto(xcor, ycor + 30)

    def move_down(self):
        xcor = turtles[0].xcor()
        ycor = turtles[0].ycor()
        if ycor > -225:
            turtles[0].goto(xcor, ycor - 30)

    def bot_movement(self):
        xcor = turtles[1].xcor()
        ycor = turtles[1].ycor()
        if ycor < 220 and self.new_y > 1 or ycor > -220 and self.new_y < 1:
            turtles[1].goto(xcor, ycor + self.new_y)
        elif ycor == 220:
            self.botdown()
        elif ycor == -220:
            self.botdown()

    def botdown(self):
        self.new_y *= -1
