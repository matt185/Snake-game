# import the module

import turtle
import random

# declare variable 

# setup the screen 

game_area = turtle.Screen()
game_area.title("Snake Game")
game_area.bgcolor("lightgreen")
game_area.setup(width=500, height=500)
game_area.tracer(0) # for control of the animation 

# set the snake head

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup() 
head.goto(random.randint(-245, 245),random.randint(-245, 245))
head.direction = "stop" # at the beginning the speed is 0

body_part = []

# set the token

token = turtle.Turtle()
token.speed(0)
token.shape("square")
token.color("purple")
token.penup()

if head.distance(token) < 10:   
    x = random.randint(-245, 245)
    y = random.randint(-245, 245)
    token.goto(x,y)
else:
    token.goto(random.randint(-245, 245),random.randint(-245, 245))

# set the control and movement  
def up_direction():
    head.direction = "up"

def down_direction():
    head.direction = "down"
    
def left_direction():
    head.direction = "left"

def right_direction():
    head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 10)
    
    if head.direction == "down":
        head.sety(head.ycor() - 10)
    
    if head.direction == "right":
        head.setx(head.xcor() + 10)
        
    if head.direction == "left":
        head.setyx(head.xcor()+10)

    



# set the game
while True:
   game_area.update()

game_area.mainloop()


