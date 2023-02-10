import random
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Score_board
from ball import COLORS_LST

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
l_paddle = Paddle((-380, 0))  # left paddle object
r_paddle = Paddle((380, 0))  # right paddle object
repeat = True
ball = Ball()  # ball object
r_score_turtle = Score_board()  # turtle object for tracking right side score
l_score_turtle = Score_board()  # turtle object for tracking left side score

while r_score_turtle.repeat and l_score_turtle.repeat:
    screen.listen()
    screen.onkeypress(key='w', fun=l_paddle.go_up)
    screen.onkeypress(key='s', fun=l_paddle.go_down)
    screen.onkeypress(key='Up', fun=r_paddle.go_up)
    screen.onkeypress(key='Down', fun=r_paddle.go_down)

    game_is_on = True
    while game_is_on:
        time.sleep(0.030)

        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_on_wall()
        if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
            ball.bounce_on_paddle(r_paddle)
            r_paddle.color(random.choice(COLORS_LST))

        elif ball.distance(l_paddle) < 50 and ball.xcor() < -350:
            ball.bounce_on_paddle(r_paddle.xcor())
            l_paddle.color(random.choice(COLORS_LST))

        if ball.xcor() > 390 or ball.xcor() < -390:
            if ball.xcor() > 390:  # ball is with right paddle
                l_score_turtle.score_display((-200, 255), score=1)
                r_score_turtle.score_display((200, 255), score=-1)

            else:  # ball is with left paddle
                l_score_turtle.score_display((-200, 255), score=-1)
                r_score_turtle.score_display((200, 255), score=1)

            game_is_on = False
            ball.relocation()
            r_paddle.paddle_relocation(position=(380, 0), new_relocation=True)
            l_paddle.paddle_relocation(position=(-380, 0), new_relocation=True)
            time.sleep(2)

screen.exitonclick()
