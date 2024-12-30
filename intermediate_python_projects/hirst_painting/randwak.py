import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]
tim.pensize(15)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


for _ in range(200):
    tim.speed(10)
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


