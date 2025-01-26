import random
import turtle
import pygame# type: ignore
import time, datetime
#movie = input("do you want to watch a movie or music, or do you want to play?")
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
aimport random
import turtle
import pygame# type: ignore
import time, datetime
#movie = input("do you want to watch a movie or music, or do you want to play?")
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
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(-300,0)
ball.dx = 0.3
ball.dy = 0.2

ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("yellow")
ball1.penup()
ball1.goto(300,0)
ball1.dx = -0.3
ball1.dy = -0.2
#Add another ball



balls = [ball,ball1]

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
miss_chance = 0.9
def ai_move(paddle, ball):
    # AI has a random chance to miss the ball
    
    if random.random() > miss_chance:  # 80% chance to move
        if paddle.ycor() < ball.ycor() and paddle.ycor() < 250:  # Avoid paddle out of screen
            if paddle == paddle_a:
                paddle_a_up()
            else:
                paddle_b_up()
        elif paddle.ycor() > ball.ycor() and paddle.ycor() > -240:  # Avoid paddle out of screen
            if paddle == paddle_a:
                paddle_a_down()
            else:
                paddle_b_down()




# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(bye,"/")

while True:
    wn.update()
    for ball in balls:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            
        if ball.xcor() > 350:
            ball.goto(300,0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("player A: {}  player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
        if ball.xcor() < -350:
            ball.goto(-300,0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("player A: {}  player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
#paddle and ball collisions

        if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1
            
        if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
            
        if score_b == 50:
            wn.clear()
            wn.bgcolor("red")
            pen.color("blue")
            pen.goto(0,0)
            pen.write('GAME OVER',align="Center",font=("Courier",70,"normal"))
            time.sleep(2)
            turtle.bye()
            #time.sleep(1)
            end_time = time.time()  # end the timer
            elapsed_time = int(end_time - start_time)   # calculate the elapsed time
            # a = datetime.datetime.fromtimestamp(start_time)
            # b = datetime.datetime.fromtimestamp(end_time)
            # readable_time= a.time()
            # readable_time2= b.time()
            # print(f"this is the end_time: {readable_time}, and this is the start_time: {readable_time2}")
            print(f"Elapsed time: {elapsed_time} seconds")
            break
        
    
        
        if score_a == 50:
            wn.clear()
            wn.bgcolor("red")
            pen.color("blue")
            pen.goto(0,0)
            pen.write('You win',align="Center",font=("Courier",70,"normal"))
            time.sleep(2)
            turtle.bye()

            
            
#AI player

    for ball in balls:
       
        ai_move(paddle_b, random.choice(balls))


    
#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(-300,0)
ball.dx = 0.3
ball.dy = 0.2

ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("yellow")
ball1.penup()
ball1.goto(300,0)
ball1.dx = -0.3
ball1.dy = -0.2
#Add another ball



balls = [ball,ball1]

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
miss_chance = 0.9
def ai_move(paddle, ball):
    # AI has a random chance to miss the ball
    
    if random.random() > miss_chance:  # 80% chance to move
        if paddle.ycor() < ball.ycor() and paddle.ycor() < 250:  # Avoid paddle out of screen
            if paddle == paddle_a:
                paddle_a_up()
            else:
                paddle_b_up()
        elif paddle.ycor() > ball.ycor() and paddle.ycor() > -240:  # Avoid paddle out of screen
            if paddle == paddle_a:
                paddle_a_down()
            else:
                paddle_b_down()




# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(bye,"/")

while True:
    wn.update()
    for ball in balls:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            
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
            
        if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
            
        if score_b == 50:
            wn.clear()
            wn.bgcolor("red")
            pen.color("blue")
            pen.goto(0,0)
            pen.write('GAME OVER',align="Center",font=("Courier",70,"normal"))
            time.sleep(2)
            turtle.bye()
            #time.sleep(1)
            end_time = time.time()  # end the timer
            elapsed_time = int(end_time - start_time)   # calculate the elapsed time
            # a = datetime.datetime.fromtimestamp(start_time)
            # b = datetime.datetime.fromtimestamp(end_time)
            # readable_time= a.time()
            # readable_time2= b.time()
            # print(f"this is the end_time: {readable_time}, and this is the start_time: {readable_time2}")
            print(f"Elapsed time: {elapsed_time} seconds")
            break
        
    
        
        if score_a == 50:
            wn.clear()
            wn.bgcolor("red")
            pen.color("blue")
            pen.goto(0,0)
            pen.write('You win',align="Center",font=("Courier",70,"normal"))
            time.sleep(2)
            turtle.bye()

            
            
#AI player

    for ball in balls:
       
        ai_move(paddle_b, random.choice(balls))


    
