from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(self.score, align= ALIGNMENT, font=FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
