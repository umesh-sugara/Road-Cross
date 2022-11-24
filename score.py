from turtle import Turtle
FONT = ('Courier', 20, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.write(f'Level: {self.level}',align='left', font=FONT)
    
    def levelUp(self):
        self.level+=1
        self.clear()
        self.goto(-260,260)
        self.write(f'Level: {self.level}',align='left', font=FONT)
    
    def gameUp(self):
        self.clear()
        self.goto(0,0)
        self.write(f'Accident!! Your level was: {self.level}',align='center', font=('Ariel',20,'bold'))
