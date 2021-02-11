from turtle import Turtle
class State(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.hideturtle()
        self.name = ""


    def name_state(self,name):
        self.name = name

    def move_state(self,xcor,ycor):
        self.goto(xcor,ycor)
        self.write(self.name,align="center",font=("Courier",8,"normal"))
