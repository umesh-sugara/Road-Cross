from turtle import Screen
import time
from player import Player
from car import Car
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title('Cross-Roads')



player= Player()
car = Car()
score=Score()



screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')


game_is_on =  True
while game_is_on:
    time.sleep(.1)
    screen.update()
    car.createCar()
    car.moveCar()

    for cars in car.allcars:
        if cars.distance(player) < 20:
            print('accident!!')
            score.gameUp()
            game_is_on= False

   
    if player.ycor() >= 250:
        print(f'{score.level} lap complete')
        player.goto(0,-270)
        score.levelUp()
        car.speedUp()







screen.exitonclick()
