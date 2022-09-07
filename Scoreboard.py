from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, score = 0) -> None:
        super().__init__()
        self.score = score
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center")

    def increase_score(self, score = 1):
        self.score += score
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f'Score: {self.score}', False, align="center")