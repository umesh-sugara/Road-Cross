from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DIS = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.color('Black')
        self.left(90)
        self.penup()
        self.goto(0,-270)

    def move_up(self):
        self.forward(MOVE_DIS)

    def move_down(self):
        self.backward(MOVE_DIS)
        
