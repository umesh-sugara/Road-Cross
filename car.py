from turtle import Turtle
import random

COLORS = ['red', 'green', 'yellow', 'orange', 'blue', 'pink']
X = 270
Y = 250
SHAPE = [1, 2, 3]
LANES = []


class Car(Turtle):
    def __init__(self) :
        self.allcars = []
        self.carspeed=5

    def createCar(self):
        random_chance = random.randint(1,4)
        if random_chance == 1:
            newcar = Turtle('square')
            newcar.shapesize(1, 2)
            newcar.penup()
            newcar.color(random.choice(COLORS))
            y = random.randint(-230, 230)
            newcar.goto(300, y)
            self.allcars.append(newcar)

    def moveCar(self):
        for car in self.allcars:
            car.backward(self.carspeed)

    def speedUp(self):
        self.carspeed+=5

