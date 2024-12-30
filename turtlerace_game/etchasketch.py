import turtle as t

tim = t.Turtle()
screen = t.Screen()

screen.listen()
def moves_forward():
    tim.forward(10)
def moves_backward():
    tim.backward(10)
def turn_left():
    tim.setheading(tim.heading() + 10)
def turn_right():
    tim.setheading(tim.heading() - 10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(moves_forward, "w")
screen.onkey(moves_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()