from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT_PADDLE_POSITION = (350, 0)
LEFT_PADDLE_POSITION = (-350, 0)


class Paddle(Turtle):
    def __init__(self, left_or_right):
        super().__init__(shape="square")
        self.create_paddle(left_or_right)

    def create_paddle(self, left_or_right):
        self.penup()
        self.color("white")
        self.setheading(90)
        if left_or_right == "r":
            self.goto(RIGHT_PADDLE_POSITION)
        else:
            self.goto(LEFT_PADDLE_POSITION)
        self.turtlesize(stretch_wid=1, stretch_len=5)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)
