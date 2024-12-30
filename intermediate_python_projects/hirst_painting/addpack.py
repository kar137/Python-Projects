# import heroes
# import villains
# print(heroes.gen())

from turtle import Turtle, Screen
tim_turtle = Turtle()

# for _ in range(15):
#     tim_turtle.forward(10)
#     tim_turtle.penup()
#     tim_turtle.forward(10)
#     tim_turtle.pendown()

colors = ["cyan", "chartreuse", "maroon", "slate blue", "deep pink"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim_turtle.forward(100)
        tim_turtle.right(angle)

for shapes_side_n in range(3, 11):
    draw_shape(shapes_side_n)
    import random
    tim_turtle.color(random.choice(colors))




screen = Screen()
screen.exitonclick()
