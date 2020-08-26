# import the module

import turtle
import random
import time

# declare variable 
delay = 0.05
score = 0
high_score = 0

#add new pattern
head_pic="head1.gif"
turtle.register_shape(head_pic)

wall_pic = "wall.gif"
turtle.register_shape(wall_pic)

# setup the screen 

game_area = turtle.Screen()
game_area.title("Snake Game")
game_area.bgpic("desert1.gif")
game_area.setup(width=600, height=600)
game_area.tracer(0) # for control of the animation 



# set the snake head

head = turtle.Turtle()
head.speed(0)
head.shape(head_pic)
head.color("black")
head.penup() 
head.goto(random.randint(-290, 290),random.randint(-290, 290))
head.direction = "stop" # at the beginning the speed is 0

body_part = []

#set up obstale

obstacle1 = turtle.Turtle()
obstacle1.shape(wall_pic)
obstacle1.color("gray")
obstacle1.penup()
if head.distance(obstacle1) < 10 and token.distance(obstacle1)<10  and obstacle2.distance(obstacle1)<100 and obstacle3.distance(obstacle1)<100 and obstacle4.distance(obstacle1)<100:   
    obstacle1.goto(random.randint(-250, 250),random.randint(-250, 250))
else:
    obstacle1.goto(random.randint(-250, 250),random.randint(-250, 250))

obstacle2 = turtle.Turtle()
obstacle2.shape(wall_pic)
obstacle2.color("gray")
obstacle2.penup()
if head.distance(obstacle2) < 10 and token.distance(obstacle2)<10  and obstacle1.distance(obstacle2)<100 and obstacle3.distance(obstacle2)<100 and obstacle4.distance(obstacle2)<100:   
    obstacle2.goto(random.randint(-250, 250),random.randint(-250, 250))
else:
    obstacle2.goto(random.randint(-250, 250),random.randint(-250, 250))

obstacle3 = turtle.Turtle()
obstacle3.shape(wall_pic)
obstacle3.color("gray")
obstacle3.penup()
if head.distance(obstacle3) < 10 and token.distance(obstacle3)<10  and obstacle1.distance(obstacle3)<100 and obstacle2.distance(obstacle3)<100 and obstacle4.distance(obstacle3)<100:   
    obstacle3.goto(random.randint(-250, 250),random.randint(-250, 250))
else:
    obstacle3.goto(random.randint(-250, 250),random.randint(-250, 250))

obstacle4 = turtle.Turtle()
obstacle4.shape(wall_pic)
obstacle4.color("gray")
obstacle4.penup()
if head.distance(obstacle4) < 10 and token.distance(obstacle4)<10 and obstacle1.distance(obstacle4)<100 and obstacle2.distance(obstacle4)<100 and obstacle3.distance(obstacle4)<100:   
    obstacle4.goto(random.randint(-250, 250),random.randint(-250, 250))
else:
    obstacle4.goto(random.randint(-250, 250),random.randint(-250, 250))

# set the token

token = turtle.Turtle()
token.speed(0)
token.shape("square")
token.color("darkred")
token.penup()

if head.distance(token) < 10 and obstacle4.distance(token)<10 and obstacle1.distance(token)<100 and obstacle2.distance(token)<100 and obstacle3.distance(token)<100:   
    token.goto(random.randint(-290, 290),random.randint(-290, 290))
else:
    token.goto(random.randint(-290, 290),random.randint(-290, 290))

#write text on screen

#point 

writing = turtle.Turtle()
writing.speed(0)
writing.shape("square")
writing.color("black")
writing.penup()
writing.hideturtle()
writing.goto(0,260)
writing.write("Score: 0  HighScore:0", align="center", font=("Arial", 24, "normal"))

#game over

game_over = turtle.Turtle()
game_over.speed(0)
game_over.shape("circle")
game_over.color("red")
game_over.penup()
game_over.goto(0,0)
game_over.hideturtle()


#score

res_score = turtle.Turtle()
res_score.speed(0)
res_score.shape("circle")
res_score.color("red")
res_score.penup()
res_score.goto(0,-100)
res_score.hideturtle()

#high score

res_hscore = turtle.Turtle()
res_hscore.speed(0)
res_hscore.shape("circle")
res_hscore.color("red")
res_hscore.penup()
res_hscore.goto(0,-100)
res_hscore.hideturtle()


# set the control and movement function 

def up_direction():
    if head.direction != "down":
        head.direction = "up"

def down_direction():
    if head.direction != "up":
        head.direction = "down"
    
def left_direction():
    if head.direction != "right":
        head.direction = "left"

def right_direction():
    if head.direction != "left":
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

def pause():
    head.direction = "stop"
    for part in body_part:
        part.direction= "stop"
# set keyboard keys

game_area.listen()
game_area.onkeypress(up_direction, "Up")
game_area.onkeypress(down_direction, "Down")
game_area.onkeypress(left_direction, "Left")
game_area.onkeypress(right_direction, "Right")
game_area.onkeypress(pause, "space")
 
# set the game
while True:
    game_over.clear()
    res_hscore.clear()
    res_score.clear()
    game_area.update()

    #when token hit

    if head.distance(token) < 20:
        #move it to different place
        check = 0
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        while check == 0:
            token.goto(x, y)
            
            if token in (body_part):
                break

            check=1
                
        #add a part to the body
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("green")
        new_part.shapesize(1,0.8)
        new_part.penup()
        body_part.append(new_part)
        
        score += 10
        
        if score > high_score:
            high_score = score
        writing.clear()
        writing.write("Score: {}  HighScore: {}".format(score,high_score), align="center".format(score,high_score), font=("Arial", 24, "normal"))
        #modify delay

        delay -= 0.001
    #check for obstacle collision

    if obstacle1.distance(head) < 20:
        game_over.write("GAME OVER", align="center", font= ("Arial", 44, "bold"))
        if score < high_score:
                res_score.write("FINAL SCORE {}".format(score), align="center", font=("Arial", 44, "bold"))
        else:
                res_hscore.write("NEW HIGHSCORE {}".format(high_score), align="center", font=("Arial", 44, "bold"))
        time.sleep(2)
        head.goto(random.randint(-290, 290), random.randint(-290, 290))
        head.direction = "stop"
    
    if obstacle2.distance(head) < 20:
        game_over.write("GAME OVER", align="center", font= ("Arial", 44, "bold"))
        if score < high_score:
                res_score.write("FINAL SCORE {}".format(score), align="center", font=("Arial", 44, "bold"))
        else:
                res_hscore.write("NEW HIGHSCORE {}".format(high_score), align="center", font=("Arial", 44, "bold"))
        time.sleep(2)
        head.goto(random.randint(-290, 290), random.randint(-290, 290))
        head.direction = "stop"

    if obstacle3.distance(head) < 20:
        game_over.write("GAME OVER", align="center", font= ("Arial", 44, "bold"))
        if score < high_score:
                res_score.write("FINAL SCORE {}".format(score), align="center", font=("Arial", 44, "bold"))
        else:
                res_hscore.write("NEW HIGHSCORE {}".format(high_score), align="center", font=("Arial", 44, "bold"))
        time.sleep(2)
        head.goto(random.randint(-290, 290), random.randint(-290, 290))
        head.direction = "stop"

    if obstacle4.distance(head) < 20:
        game_over.write("GAME OVER", align="center", font= ("Arial", 44, "bold"))
        if score < high_score:
                res_score.write("FINAL SCORE {}".format(score), align="center", font=("Arial", 44, "bold"))
        else:
                res_hscore.write("NEW HIGHSCORE {}".format(high_score), align="center", font=("Arial", 44, "bold"))
        time.sleep(2)
        head.goto(random.randint(-290, 290), random.randint(-290, 290))
        head.direction = "stop"
    #check boarder collision

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:

        game_over.write("GAME OVER", align="center", font= ("Arial", 44, "bold"))
        if score < high_score:
                res_score.write("FINAL SCORE {}".format(score), align="center", font=("Arial", 44, "bold"))
        else:
                res_hscore.write("NEW HIGHSCORE {}".format(high_score), align="center", font=("Arial", 44, "bold"))
        time.sleep(2)
        head.goto(random.randint(-290, 290), random.randint(-290, 290))
        head.direction = "stop"
        #remove the piece from the screen
        for part in body_part:
            part.goto(1000, 1000)
        body_part.clear()
        score = 0
        writing.clear()
        writing.write("Score: {}  HighScore: {}".format(score, high_score), align="center".format(score, high_score), font=("Arial", 24, "normal"))
        
        
        delay = 0.05

    #rearrange the body    
    for index in range(len(body_part) - 1, 0, -1):
        x = body_part[index - 1].xcor()
        y = body_part[index - 1].ycor()
        body_part[index].goto(x, y)
    
    #place the head

    if len(body_part) > 0:
        body_part[0].goto (head.xcor(),head.ycor())
     
    move()

    # check for body collision

    for part in body_part:
        if part.distance(head) < 20:
            game_over.write("GAME OVER", align="center", font=("Arial", 44, "bold"))
            if score < high_score:
                res_score.write("FINAL SCORE {}".format(score), align="center", font=("Arial", 44, "bold"))
            else:
                res_hscore.write("NEW HIGHSCORE {}".format(high_score), align="center", font=("Arial", 44, "bold"))
            time.sleep(2)
            head.goto(random.randint(-290, 290), random.randint(-290, 290))
            head.direction = "stop"
            for part in body_part:
                part.goto(1000, 1000)
            body_part.clear()
            score = 0
            writing.clear()
            writing.write("Score: {}  HighScore: {}".format(score,high_score), align="center".format(score,high_score), font=("Arial", 24, "normal"))
            delay = 0.05

    time.sleep(delay)
game_area.mainloop()


