#===================import===================

import turtle as trtl
import turtle as player
import turtle as bullet
import turtle as opponent
import turtle as sc
import random 
import math

#===================create turtle===================

player=player.Turtle()
bullet=bullet.Turtle()
opponent=opponent.Turtle()

#===================setup===================

#player
player.penup()
player.setheading(90)
player.speed(0)
player.goto(0,-300)
#Bullet
bulletready=0
bullet.penup()
bullet.speed(0)
bullet.ht()
bullet.color("white")
player.pencolor("white")
#opponent
opponent.penup()
opponent.goto(0,100)
opponent.color("white")
#timer

score=0
timer = 20
counter_interval = 1000
timer_up = False

sc=trtl.Turtle()
sc.pencolor("white")
sc.penup()
sc.goto(-470,300)
sc.ht()


font = ("Impact", 50, "bold")
sc.write("Score: " + str(score), font=font)

counter =  trtl.Turtle()
counter.pencolor("white")
counter.ht()
counter.penup()
counter.goto(200,300)

#===================create screen===================

wn = trtl.Screen()
wn.bgcolor("black")

#===================Images===================

opponent_image = "enemy4.gif"

wn.addshape(opponent_image)

player_image = "ship.gif"

wn.addshape(player_image)
player.shape(player_image) 

#===================variables===================

bulletgo = 0
bulletready = 1

#===================movement===================

def right():
    player.setheading(0)
    player.forward(5)


def left():
    player.setheading(180)
    player.forward(5)

#===================Multiple opponents===================

opponent.ht()
NumOfopponents = 5

opponents = []

for i in range(NumOfopponents):
    opponents.append(trtl.Turtle())

for opponent in opponents:
    opponent.shape(opponent_image)
    opponent.penup()
    opponent.speed(0)
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(0,100)
    opponent.setposition(new_xpos,new_ypos)

#===================bullets===================

x = player.xcor()-10
y = player.ycor()+30


bx = bullet.xcor()
by = bullet.ycor()

if by == -900:
    bulletgo == 1

def shoot():
    global bulletgo
    global bulletready
    by = bullet.ycor()
    if by == -900:
        bulletready = 1
        bulletgo = 0
    if bulletready == 0:
        bullet.ht()
    if bulletready == 1:
        x = player.xcor()-10
        y = player.ycor()+80
        bullet.st()
        bullet.goto(x,y)
        bullet.setheading(90)
        while bulletgo <= 50:
            bullet.speed(1)
            bullet.forward(10)
            bulletgo += 1
            bulletready == 0
            for opponent in opponents:
                collision(opponent, bullet)
            if bulletgo >= 50:
                bullet.speed(0)
                bullet.ht()
                bulletgo = 100
                bullet.goto(-900,-900)


#===================collision===================

def collision(t1, t2):
    global bulletgo
    tDistance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if tDistance < 25:
        t1.ht()
        new_xpos = random.randint(-400,400)
        new_ypos = random.randint(0,100)
        t1.goto(new_xpos,new_ypos)
        t1.st()
        bulletgo = 51
        score_counter()
        increase_time()

#===================score===================

def score_counter():
    global score
    score += 1000
    print(score)
    sc.clear()
    sc.write("Score: " + str(score), font=font)

#===================countdown===================

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.goto(-300,300)
    counter.write("Time's Up you lost", font=font)
    timer_up = True
    gameover()
  else:
    counter.write("Timer: " + str(timer), font=font)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#===================gameover===================

def gameover():
    player.ht()
    player.goto(10000,10000)
    wn.bgcolor("red")


#===================change position===================

def change_position ():
    opponent.speed(0)
    opponent.penup()
    opponent.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(0,100)
    opponent.goto(new_xpos,new_ypos)
    opponent.st()

#===================increase time===================

def increase_time():
    global timer
    timer += 7

#===================keypresses===================

wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(shoot,"space")

#===================listen===================

wn.listen()

#===================timer===================

wn.ontimer(countdown, counter_interval) 

#===================opponent moving===================

loop = 1
os = 1
change=0
while loop == 1:
    for opponent in opponents:
        collision(opponent, bullet)
        ox = opponent.xcor()
        oy = opponent.ycor()
        ox += os
        oy += change
        opponent.setx(ox)
        opponent.sety(oy)
        if ox >= 400:
            os *= -1
        if ox <= -400:
            os *= -1

#===================mainloop===================

wn.mainloop()