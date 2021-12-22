import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")

game_is_on = True
loop = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if loop == 6:
        cars.make_car()
        loop = 0
    cars.car_move()
    loop += 1

    for car in cars.car_list:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.is_at_finish():
        turtle.go_to_start()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()