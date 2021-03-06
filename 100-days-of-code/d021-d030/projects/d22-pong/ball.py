from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color('#F8CB2E')
        self.y_move = -3
        self.x_move = 3
        self.move_speed = 0.015

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.015
        self.bounce_x()
