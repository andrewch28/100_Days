from turtle import Turtle, Screen
import turtle as t
timmy = Turtle()
timmy.shape('turtle')
timmy.color("SteelBlue")
screen = Screen()

# # Task 1 - Square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# # Task 2 - Dash Line
# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# #Task 3 - Can't Hurt Me
# import random
# num = 3
# while num < 11:
#     screen.colormode(255)
#     timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     for _ in range(num):
#         timmy.right(360/num)
#         timmy.forward(100)
#     num += 1


# # Task 4 - Draw a Random Walk
# import random
# timmy.pensize(10)
# timmy.speed(10)
# for _ in range(100):
#     screen.colormode(255)
#     timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     timmy.forward(30)
#     timmy.right(random.choice([90,180,270,360]))

# #Task 5  Spirograph
# import random
# timmy.speed('fastest')
# t.colormode(255)
# timmy.pensize(1)
#
# angle = 0
# while angle <360:
#     timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     timmy.circle(100)
#     timmy.right(5)
#     angle += 5









screen = Screen()
screen.exitonclick()