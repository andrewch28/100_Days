from turtle import Turtle

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def print_state(self, state, x, y):
        self.goto(int(x), int(y))
        self.write(f"{state}", align = 'center', font=("Courier", 8, "normal"))
