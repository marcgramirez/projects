from turtle import Turtle, Screen
import turtle as t
import random

#timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("arrow")
#timmy_the_turtle.color("red")

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


for _ in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()