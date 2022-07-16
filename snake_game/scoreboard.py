from turtle import Turtle

ALIGNMENT = "center"
FONT_SIZE = 22
FONT = ("Arial", 22, "normal")
GAME_OVER_MESSAGE = ["GAME OVER", "press r to restart",
                     "press q to quit", "press space to speed up game"]

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.restart()

    def restart(self):
        self.reset()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def change_score(self, value):
        self.score += value
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        indent = 0
        for message in GAME_OVER_MESSAGE:
            self.write(message, align=ALIGNMENT, font=FONT)
            indent -= FONT_SIZE + 10
            self.goto(0, indent)