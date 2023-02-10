import random
from turtle import Turtle

COLORS_LST = ['red', 'purple', 'violet', 'pink', 'SkyBlue', 'tomato', 'gold', 'chartreuse', 'cyan', 'DarkMagenta',
              'DarkCyan', 'DarkOrchid1', 'DeepPink1', 'DarkOrange1', 'coral2']


class Ball(Turtle):  # Inheriting the turtle object

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.shape('circle')
        self.shapesize(1)
        self.goto(random.randint(-50, 50), random.randint(-0, 0))
        self.x_move = [10, -10]
        self.y_move = [-10, 10]
        self.incremental_y = 0
        self.incremental_x = 0
        self.incremental_velocity()

    def incremental_velocity(self):
        self.incremental_y = random.choice(self.y_move)
        self.incremental_x = random.choice(self.x_move)

    def move(self):
        new_y = self.ycor() + self.incremental_y
        new_x = self.xcor() + self.incremental_x
        self.goto(new_x, new_y)

    # relocation to a point in plane where player can easily pick the ball
    def relocation(self):
        self.goto(random.randint(-50, 50), random.randint(-0, 0))
        self.incremental_velocity()
        self.disco_colors()

    def disco_colors(self):
        self.color(random.choice(COLORS_LST))

    def bounce_on_wall(self):
        # change the sign of the y co-ordinate to bounce the ball
        self.incremental_y *= -1
        self.disco_colors()

    def bounce_on_paddle(self, paddle_x_position):
        if paddle_x_position == 380:  # ball is at right paddle
            self.incremental_x = abs(self.incremental_x)
            self.incremental_x *= 1.020
            self.incremental_y *= 1.020
            self.disco_colors()

        else:  # means ball is at left paddle
            self.incremental_x = -abs(self.incremental_x)
            self.incremental_x *= 1.020
            self.incremental_y *= 1.020
            self.disco_colors()
