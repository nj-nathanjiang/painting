import random
import turtle as t


t.colormode(255)
color_list = [(240, 238, 233), (235, 238, 244), (245, 238, 242), (238, 244, 240), (182, 163, 132), (144, 162, 183),
              (125, 98, 68), (179, 151, 164), (182, 99, 127), (123, 82, 97)]

tim = t.Turtle()
tim.shape("turtle")
tim.color("dark green")
tim.penup()
tim.right(90)
tim.forward(225)
tim.right(90)
tim.forward(225)


def draw_circle():
    tim.dot(20, random.choice(color_list))


for i in range(10):
    draw_circle()
    tim.right(180)
    for m in range(9):
        tim.forward(50)
        draw_circle()
    tim.right(180)
    tim.right(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(450)
tim.hideturtle()

screen = t.Screen()
screen.exitonclick()
