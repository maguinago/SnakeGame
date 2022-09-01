from turtle import Turtle


class Score (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_high_score()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.ht()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", move=False, align="center", font=("Courier", 12, "normal"))

    def increase(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > int(self.high_score):
            with open("high_score.txt", mode="w") as hs:
                hs.write(str(self.score))
        self.read_high_score()
        self.score = 0
        self.update()

    def read_high_score(self):
        with open("high_score.txt") as hs:
            self.high_score = int(hs.read())
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, "center", ("Courier", 16, "normal"))
