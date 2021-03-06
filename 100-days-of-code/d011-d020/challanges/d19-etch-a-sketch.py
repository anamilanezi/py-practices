from turtle import Turtle, Screen

# W = forwards
# S = backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear and go back to center

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_screen():
    tim.reset()

tim.speed(0)
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
