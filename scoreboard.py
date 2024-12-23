from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = open("data.txt", mode="r").read()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int( self.high_score):
            self.high_score = self.score
            d = open("data.txt", mode="w")
            d.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
