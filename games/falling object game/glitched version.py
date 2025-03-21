import turtle
import random
import pygame#type ignore
import time
from datetime import datetime
from tkinter import messagebox


pygame.mixer.init()

score = 0
lives = 10

wn = turtle.Screen()
wn.title("falling objects game")
wn.bgcolor("blue")
wn.bgpic(r"falling-object-game\img\forest.gif")
wn.setup(width=800,height=600)
wn.tracer(14)
wn.addshape(r"falling-object-game\img\deer_right.gif")
wn.addshape(r"falling-object-game\img\acorn.gif")
wn.addshape(r"falling-object-game\img\hunter_right.gif")


player = turtle.Turtle()
player.speed(0)
player.shape(r"falling-object-game\img\deer_right.gif")
player.color("white")
player.penup()
player.goto(0,-250)
player.direction = "stop"

good_guys = []
for _ in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape(r"falling-object-game\img\acorn.gif")
    good_guy.color("blue")
    good_guy.penup()
    x = random.randint(-380,380)
    y = random.randint(300,400)
    good_guy.goto(x,y)
    good_guy.speed = random.randint(1, 10)
    good_guys.append(good_guy)


bad_guys = []
for _ in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape(r"falling-object-game\img\hunter_right.gif")
    bad_guy.color("red")
    bad_guy.penup()
    x = random.randint(-380,380)
    y = random.randint(300,400)
    bad_guy.goto(x,y)
    bad_guy.speed = random.randint(0, 1)
    bad_guys.append(bad_guy)


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.hideturtle()
pen.penup()
pen.goto(0,260)
font = ("Courier",30,"normal")
pen.write("Score:{}  Lives:{}".format(score, lives), align= "Center",font=font)


def go_left():
    player.direction = "left"
def go_right():
    player.direction = "right"
def go_up():
    player.direction = "up"
def go_down():
    player.direction = "down"

#keyboard bindings
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")

while True:
    wn.update()
    if player.direction == "left":
        x = player.xcor()
        if x > -380:  # Only move left if not at the left edge
            x -= 3
        player.setx(x)
    if player.direction == "right":
        x = player.xcor()
        if x < 380:  # Only move right if not at the right edge
            x += 3
        player.setx(x)
    if player.direction == "up":
        y = player.ycor()
        y += 3
        player.sety(y)
    if player.direction == "down":
        y = player.ycor()
        y -= 3
        player.sety(y)
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)

        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            good_guy.goto(x,y)
        if good_guy.distance(player) < 20:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            good_guy.goto(x,y)
            score += 1
            pen.clear()
            pen.write("Score:{}  Lives:{}".format(score, lives),align="Center",font=font)
    

    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            bad_guy.goto(x,y)
        if bad_guy.distance(player) < 20:
            x = random.randint(-380,380)
            y = random.randint(200,400)
            bad_guy.goto(x,y)
            score -= 1
            lives -= 1
            pen.clear()
            pen.write("Score:{}  Lives:{}".format(score, lives),align="Center",font=font)
    
    if player.xcor() <= -380:
        player.direction = "stop"
    if player.xcor() >= 380:
        player.direction = "stop"

    if lives <= 0:
        if messagebox.askyesno("Game Over", "Play again?") == True:
                lives = 10
                score = 0
                player.speed = 0
                player.goto(0,-250)
                player.setheading(0)
                pen.clear()
                pen.write("Score:{}  Lives:{}".format(score, lives),align="Center",font=font)

        else:
            exit()

wn.mainloop()
