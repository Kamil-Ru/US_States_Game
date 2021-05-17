from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class State(Turtle):
    def __init__(self, x_cor, y_cor, state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.x = x_cor
        self.y = y_cor
        self.goto(self.x, self.y)
        self.state = state
        self.write(f"{self.state}", align=ALIGNMENT, font=FONT)





