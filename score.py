from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("car") as file:
            high_score = int(file.read())
            self.high_score = high_score
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score {self.score} High Score: {self.high_score}", align='center', font=("Arial", 10, "normal"))

    def scoring(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            with open("car", 'w') as file:
                file.write(str(self.score))
            self.high_score = self.score

        self.score = 0
        self.update()
