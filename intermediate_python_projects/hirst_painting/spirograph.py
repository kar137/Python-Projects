import turtle as t
tim = t.Turtle()
import random
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

tim.speed("fastest")


def spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(80)
        tim.setheading(tim.heading() + gap_size)

spirograph(5)
screen = t.Screen()
screen.exitonclick()