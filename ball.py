from turtle import Turtle
class Ball(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1,1)
        self.goto(pos)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.09
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.09


