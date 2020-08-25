# import the module

import turtle
import random
import time

# declare variable 
delay= 0.05
# setup the screen 

game_area = turtle.Screen()
game_area.title("Snake Game")
game_area.bgcolor("lightgreen")
game_area.setup(width=600, height=600)
game_area.tracer(0) # for control of the animation 

# set the snake head

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup() 
head.goto(random.randint(-290, 290),random.randint(-290, 290))
head.direction = "stop" # at the beginning the speed is 0

body_part = []

# set the token

token = turtle.Turtle()
token.speed(0)
token.shape("square")
token.color("purple")
token.penup()

if head.distance(token) < 10:   
    token.goto(random.randint(-290, 290),random.randint(-290, 290))
else:
    token.goto(random.randint(-290, 290),random.randint(-290, 290))


# set the control and movement function 

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
        head.sety(head.ycor() + 20)
  
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    
    if head.direction == "right":
        head.setx(head.xcor() + 20)
        
    if head.direction == "left":
        head.setx(head.xcor()-20)

# set keyboard keys

game_area.listen()
game_area.onkeypress(up_direction, "Up")
game_area.onkeypress(down_direction, "Down")
game_area.onkeypress(left_direction, "Left")
game_area.onkeypress(right_direction, "Right")

 
# set the game
while True:
    game_area.update()

    #when token hit
    if head.distance(token) < 20:
        #move it to different place
        token.goto(random.randint(-290, 290), random.randint(-290, 290))

        #add a part to the body
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("violet")
        new_part.penup()
        body_part.append(new_part)
    #rearrange the body    
    for index in range(len(body_part) - 1, 0, -1):
        x = body_part[index - 1].xcor()
        y = body_part[index - 1].ycor()
        body_part[index].goto(x, y)
    
    #place the head

    if len(body_part) > 0:
        body_part[0].goto (head.xcor(),head.ycor())
     
        
    move()
    time.sleep(delay)
game_area.mainloop()


