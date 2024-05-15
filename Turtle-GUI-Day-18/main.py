# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# color = []
#
# for i in colors:
#     color.append((i.rgb.r, i.rgb.g, i.rgb.b))
#
# print(color)

color_list = [(208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]

from turtle import Turtle, Screen


tim = Turtle()
tim.speed(30)
import random
screen = Screen()
screen.colormode(255)
y = -300
print(random.choice(color_list))
tim.teleport(-370,-300)
for _ in range (10):
    for _ in range(10):
        choice = random.choice(color_list)
        tim.pencolor(choice)
        tim.fillcolor(choice)
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()
        tim.penup()
        tim.forward(80)
    y += 70
    tim.teleport(-370, y)


screen = Screen()
screen.exitonclick()