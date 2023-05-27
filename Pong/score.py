from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

scoreboards = []


class Scoreboard(Turtle):
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        scoreboards.append(self)
        self.another_score()
        self.update_scoreboard()
        self.update_bot_scoreboard()

    def another_score(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        scoreboards.append(self)
        self.update_scoreboard()
        self.update_bot_scoreboard()

    def update_scoreboard(self):
        scoreboards[0].goto(100, 200)
        self.write(f"{self.score1}", align=ALIGNMENT, font=FONT)

    def update_bot_scoreboard(self):
        scoreboards[1].goto(-100, 200)
        self.write(f"{self.score2}", align=ALIGNMENT, font=FONT)

    def increase_score1(self):
        self.score1 += 1

    def increase_score2(self):
        self.score2 += 1

    def new_score_bot(self):
        self.increase_score2()
        self.clear()
        self.update_bot_scoreboard()
        self.update_scoreboard()

    def new_score_player(self):
        self.increase_score1()
        self.clear()
        self.update_bot_scoreboard()
        self.update_scoreboard()
