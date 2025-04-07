from turtle import Turtle

SCORE = 0
AlIGNMENT = "center"
FONT = ("Courier", 80, "bold")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.goto(position)
        self.penup()
        self.color("white")
        self.write(self.score, align=AlIGNMENT, font=FONT)
        self.hideturtle()
        
    def game_over(self):
        self.goto(0,0)        
        self.write("GAME OVER", align=AlIGNMENT, font=FONT)
        
    def scored_point(self):
        self.clear()
        self.score+=1
        self.write(self.score, align=AlIGNMENT, font=FONT)



        
    