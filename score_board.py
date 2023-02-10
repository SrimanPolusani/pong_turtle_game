from turtle import Turtle


class Score_board(Turtle):  # Inheriting the turtle object
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.repeat = True

    def score_display(self, position, score):
        self.clear()
        self.position = position
        self.goto(position)
        self.score = score + self.score

        self.write(arg=f'Score: {self.score}', font=('Arial', 15, 'italic'), align='left')
        if self.position == (200, 255) and self.score > 2:  # which is right
            self.goto(-159, 0)
            self.write(arg='Game Over! Right Side Won', font=('Arial', 20, 'italic'))
            self.repeat = False
        elif self.position == (-200, 255) and self.score > 2:  # which is left
            self.goto(-159, 0)
            self.write(arg='Game Over! Left Side Won', font=('Arial', 20, 'italic'))
            self.repeat = False
