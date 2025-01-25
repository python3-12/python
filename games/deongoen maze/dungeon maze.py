import turtle
import math
import random
import time


wn = turtle.Screen()
wn.bgcolor("brown")
wn.title("A maze game")
wn.setup(700,700)
wn.tracer(0)


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class Pene(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.hideturtle()
    def display_score(self, score):
        # Clear previous score and write new score at top
        self.clear()
        self.goto(0, 290)  # Position at the top of the screen
        self.write('Gold: {}'.format(score), align="center", font=("Courier", 40, "normal"))
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.lives = 5
        self.gold = 0
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance < 5:
            return True
        else:
            return False
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)


class Tresure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
    def destroy(self):
        self.goto(200000000,2000000000)
        self.hideturtle()


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction = random.choice(["up","down","left","right"])
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0
        
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction = random.choice(["up","down","left","right"])

        turtle.ontimer(self.move,t= random.randint(100,300))
    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance < 75:
            return True
        else:
            return False
    def destroy(self):
        self.goto(200000000,2000000000)
        self.hideturtle()

    
levels = [""]


level_1 = [
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BP BBBBBBB   E             BBE    B    TE  BB  BBBB     E   T  BBB",
    "B  BBBBBBB  BBBBBB         BTETB  B   BB   BB    BB   BB  BBB  BBB",
    "B       BB  BBBBBB  BBBBB  BBBBB  B   BB   BB        BBB  BBB  BBB",
    "BBBBB   BB  BBB   E   EBB  B  B   B   BB   BB      EBBBB  BBB  BBB",
    "BBBBB   BB  BBB  E      B  B  B   B   BB   BB  BEBBBBBBB  BBBBBBBB",
    "BBBBB   BB  BBBBBBB  BB B  B  B   B   BB   BB  BBBBBBBBB TBBBBBBBB",
    "BBBBB   BB    BBBBB TBBTB            BBB T EB  B  B    T      BBBB",
    "BBBBB         BBBBB  BB B  B  B   BBBBBB          B  EBBBBBBBBBBBBB",
    "B        BBBBBBBBBBBBBB B  B  B  EBBBBBBBBBBBE B  B   BBBBBBBBBBBBB",
    "BBBBBBB         BB    B B  BBBB        ET      B  B        BB   BBB",
    "BBBBBBBBBBBBBB  BB  BBB    BBBBBBBBBBBB  BBBBBTB       BB  BB   BBB",
    "BBBBBBBBBBBBBB  BB  BBB B  BBBBB         BB   BB       BB  BB   BBB",
    "BB       TBBBBE     BBBTB  B      BB   BB     BB   BBBBBB  BB   BBB",
    "BB  BB BBBBBBB  BBB BBB B  B      BBT  BB    BB        T   T    BBB",
    "B E               B   B B  B   E  B    BB         BBBBBBBB  BBBBBBB",
    "B BBBBB  BBBBBBBB     B    B      B  BBBB     BB  BBTTTBBB  B   BBB",
    "BT       BBBBBBBB  BBBB B     B   B  BBBB    EBB TBBTTTBBB  B   BBB",
    "BBBBBBBBBBBBBBBBB     B B  B   BBBB EBBBB     BB  BBTTTBBBEEBT  BBB",
    "BBBBBBBBTEBBBBBBB  B  B B  BBBBBBBB  BBBB  E  BB  BBTTTBBBEEB   BBB",
    "BBB TBBB           B  B B  BB  E BBBBBBBB     BB  BBEEEBBBEEB   BBB",
    "BBB     BBBBB  BBBBB   TB      BBBBBBBBT      BB  BBEEEBBBEEB   BBB",
    "BBB EBB EBBBB  BBBE   B B  BBBBBBBB EB    BBB  BT  E       E   BBB",
    "BBB  BBT       BBB  BBB B      E     B   BBBBBBBBBBBBBBBBBBB  BBBBB", 
    "BBB  BBBBBBBB  BBBBBBBB B   B   T    B   BBBBBBBBBBBBBBBBBBB  BBBBB",
    "BBB     E  E        E   B   BBBBBBBBBB  T                      T  B",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"]

tresures = []
enemys = []


levels.append(level_1)


def setup_maze(level):
    for y in range (len(level)):
        for x in range (len(level[y])):
            charecter = level[y][x]
            screen_x = -288 + (x* 24)
            screen_y = 288 - (y*24)
            if charecter == "B":
                pen.goto(screen_x,screen_y)
                pen.shape("square")
                pen.stamp()
                walls.append((screen_x,screen_y))
            if charecter == "P":
                player.goto(screen_x,screen_y)
            if charecter == "T":
                tresures.append(Tresure(screen_x,screen_y))
            if charecter == "E":
                enemys.append(Enemy(screen_x,screen_y))
    pene.display_score(player.gold)

pen = Pen()
pene = Pene()
player = Player()

walls = []


setup_maze(levels[1])

wn.listen()
wn.onkeypress(player.go_right,"Right")
wn.onkeypress(player.go_left,"Left")
wn.onkeypress(player.go_up,"Up")
wn.onkeypress(player.go_down,"Down")

wn.tracer(0)

for enemy in enemys:
    turtle.ontimer(enemy.move,t= 250)

while True:
    for tresure in tresures:
        if player.is_collision(tresure):
            player.gold += tresure.gold
            pene.display_score(player.gold)
            tresure.destroy()
            tresures.remove(tresure)
    for enemy in enemys:
        if player.is_collision(enemy):
            wn.clear()
            pen.goto(0,0)
            pene.goto(0,140)
            pene.write('PLAYERGOLD:{}'.format(player.gold),align="Center",font=("Courier",55,"normal"))
            pen.write('GAME OVER'.format(),align="Center",font=("Courier",70,"normal"))
            time.sleep(5)
            turtle.bye()
            break
    
    wn.update()
wn.mainloop()
