from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0, 480)
        self.game_on = True


    def update_score(self):
        self.clear()
        try:
            with open("snake_hs.txt", "r") as hs:
                high_score = int(hs.read())
        except ValueError:
            with open("snake_hs.txt", "w") as hs:
                hs.write("0")
            high_score = 0

        self.write(f"Score: {self.score} Highscore: {high_score}",
                   move=False, align='center', font=('Arial', 12, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Arial', 24, 'normal'))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        self.game_over()

        self.game_on = False

