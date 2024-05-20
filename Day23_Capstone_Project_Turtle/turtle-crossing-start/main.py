import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

screen.onkey(player.move, "Up")
cars = CarManager()
scoreboard= Scoreboard()

counter = 4
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter % 4 == 0:
        cars.create_car()

    cars.going_left()
    counter += 1

    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.finish()
        scoreboard.increase_level()
        cars.increase()

screen.exitonclick()