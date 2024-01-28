from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        self.move = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape('triangle')
        self.shapesize(2, 1)
        self.seth(90.0)
        self.setx(self.move)
        self.sety(-450)
        self.showturtle()
        self.color('white')

    def move_right(self):
        if self.xcor() != 320:
            self.move += 20
            self.setx(self.move)
        else:
            pass

    def move_left(self):
        if self.xcor() != -320:
            self.move -= 20
            self.setx(self.move)
        else:
            pass


