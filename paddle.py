from turtle import Turtle


class Paddle(Turtle):  # Inheriting the turtle object

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.speed('fastest')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.new_x = 0
        self.new_y = 0
        self.paddle_down_increment = 40
        self.paddle_up_increment = -40
        self.new_relocation = False

    # function for moving paddle up
    def go_up(self):
        self.new_y = self.ycor() + self.paddle_down_increment
        self.new_x = self.xcor()
        if 250 > self.new_y > -250:
            self.goto(x=self.xcor(), y=self.new_y)

    # function for moving paddle down
    def go_down(self):
        self.new_y = self.ycor() + self.paddle_up_increment
        self.new_x = self.xcor()
        if 250 > self.new_y > -250:
            self.goto(x=self.new_x, y=self.new_y)

    # function for relocating the paddle after one match
    def paddle_relocation(self, position, new_relocation):
        self.goto(position)
        self.paddle_down_increment *= 1.020
        self.paddle_up_increment *= 1.020
        while new_relocation:
            self.paddle_up_increment = -40
            self.paddle_down_increment = 40
            new_relocation = False  # breaks the loop
