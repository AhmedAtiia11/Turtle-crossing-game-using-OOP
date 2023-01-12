from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.penup()
        self.goto(-250,250)
        self.hideturtle()
        self.update()

    def update(self):
        self.level+=1
        self.clear()
        self.write(f"Level {self.level}",font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=FONT)


    


