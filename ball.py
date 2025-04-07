from turtle import Turtle

SPEED = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
        #self.shapesize(0.5,0.5,0.5)
        self.x_move = 10
        self.y_move = 10


    #Defining a function that will move the ball as long as the game is on
    def move(self):
        self.penup()
        current_x = self.xcor()
        current_y = self.ycor()
        self.speed(SPEED)
        self.goto(current_x + self.x_move, current_y + self.y_move)


    def bounce(self):
        #self.x_move = -self.x_move
        self.y_move = -self.y_move

    def hit(self):
        self.x_move = -self.x_move
        
    
    def reset_ball(self):
        self.goto(0,0)
        self.x_move = -self.x_move



# xx First the ball has to be created and put on the middle
  # xx When the game starts, the ball should start moving to the right
  # xx The movement will happen on a diagonal line, e.g. go right 20 and go left 20 and this should be repeated
  # in a loop as long as the game is on and until it hits the paddle
  # If the ball hits the paddle, then it should change its direction e.g. from gooing 20 right and 20 up it will go
  # -20 in x and still go up
  # If the ball does not hit the paddle, then the game is off





  # Change of direction

  # If ball hits paddle -> x direction changes, that means x > 280 or smaller than -280 and the same location as paddle
  # or as one part of the paddle, any part
  # If ball hits top or bottom wall -> y direction changes