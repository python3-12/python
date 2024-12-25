import turtle
import pygame# type: ignore
import time
start_time = time.time()
pygame.mixer.init()
wn = turtle.Screen()
wn.title("ping pong!")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)
score_a = 0
score_b = 0
#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
#ball
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("yellow")
ball1.penup()
ball1.goto(0,0)
ball1.dx = 0.3
ball1.dy = -0.2
#Add another ball
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color('red')
ball2.penup()
ball2.goto(0,0)
ball2.dx = -0.1
ball2.dy = -0.2
balls = [ball1,ball2]

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0  player B: 0",align="center",font=("Courier",24,"normal"))
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
def bye():
    turtle.bye()

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(bye,"l")
while True:
    wn.update()
    for ball in balls:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            sound = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\explosion.mp3")
            sound.play()
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            soundl = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\explosion.mp3")
            soundl.play()
        if ball.xcor() > 350:
            ball.goto(0,0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("player A: {}  player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
        if ball.xcor() < -350:
            ball.goto(0,0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("player A: {}  player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
#paddle and ball collisions

        if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1
            sound3 = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\lazer.mp3")
            sound3.play()
        if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
            sound4 = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\lazer.mp3")
            sound4.play()
        if score_b > 10:
            turtle.bye()
            break
            
        if score_b > 10:
            end_time = time.time()  # end the timer

            elapsed_time = end_time - start_time   # calculate the elapsed time
            
            print("Elapsed time:" + elapsed_time + "seconds")
            turtle.end_poly()
            
#AI player
    closest_ball = balls[0]
    for ball in balls:
        if ball.xcor() > closest_ball.xcor():
            closest_ball = ball

    
    if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10:
        paddle_b_up()
    elif paddle_b.ycor() > closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10:
        paddle_b_down()

    

    
