import turtle
import random
import time
print("same controls as space war, just no shooting")
time.sleep(2)
turtle.bgcolor("maroon")
turtle.speed(0)
turtle.title("Yosef's own game(made by yosef)")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)
class Sprite(turtle.Turtle):
       def __init__(self,spriteshape,color,startx,starty):
              turtle.Turtle.__init__(self,shape= spriteshape)
              self.speed(0)
              self.penup()
              self.color(color)
              self.fd(0)
              self.goto(startx,starty)
       def move(self):
            self.fd(self.speed)
            if self.xcor() > 290 :
                    self.rt(60)
                    self.setx(290)

            if self.xcor() < -290 :
                    self.rt(60)
                    self.setx(-290)

            if self.ycor() > 290 :
                    self.rt(60)
                    self.sety(290)

            if self.ycor() < -290 :
                    self.rt(60)
                    self.sety(-290)
       
class Enemy(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
            Sprite.__init__(self,spriteshape,color,startx,starty)
            self.shapesize(stretch_wid=2,stretch_len=2,outline=None)
            self.speed = 6
            self.setheading(random.randint(0,360))

class Player(Sprite):
      def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self,spriteshape,color,startx,starty)
            turtle.shapesize(stretch_len=0.2,stretch_wid=0.2,outline=None)
            self.speed(0)
            self.penup()
            self.color(color)
            self.fd(0)
            self.goto(startx,starty)
            self.speed = 1
            self.size = 1
      def turn_left(self):
                    self.lt(45)

      def turn_right(self):
                        self.rt(45)

      def accelerate(self):
                    self.speed += 1
                    

      def deccelerate(self):
                        self.speed -=1
      def is_collision(self,other):
           if (self.xcor() >= (other.xcor() - 20))and \
           (self.xcor() <= (other.xcor() + 20))and \
           (self.ycor() >= (other.ycor() - 20))and \
           (self.ycor() <= (other.ycor() + 20)):
              return True
           else:
            return False
      def increase_size(self):
        self.size += 1
        turtle.shapesize(stretch_wid=self.size, outline=None)
class Fruit(turtle.Turtle):
        def __init__(self,fruitshape,color):
            turtle.Turtle.__init__(self,shape=fruitshape)
            self.speed(0)
            self.penup()
            self.color(color)
            self.fd(0)
        def spawn_fruit(self):
                distance_from_player = 2  # Minimum distance from the player
                while True:
                    x = random.randint(-290, 290)
                    y = random.randint(-290, 290)
                    # Check if the new position is far enough from the player
                    if player.distance(x, y) > distance_from_player:
                        self.goto(x, y)
                        break
#            self.goto(random.randint(-290,290))
            # self.setheading(random.randint)

class Game():
       def __init__(self):
              self.level = 1
              self.score = 0
              self.state = "playing"
              self.pen = turtle.Turtle()
              self.lives = 10
       def draw_border(self):
              self.pen.speed(0)
              self.pen.color("black")
              self.pen.pensize(3)
              self.pen.penup()
              self.pen.goto(-300,300)
              self.pen.pendown()
              for side in range(4):
                     self.pen.fd(600)
                     self.pen.rt(90)
              self.pen.penup()
              self.pen.ht()
              self.pen.pendown()
       def show_status(self):
            self.pen.undo()
            msg = "Score: %s" % (self.score)
            self.pen.penup()
            self.pen.goto(-300, 300)
            self.pen.write(msg, font=("Arial", 16, "normal"))



fruit=Fruit("square","gray")
player = Player("square","aqua",0,0)
enemy = Enemy("classic","blue",0,100)
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
turtle.onkey(player.deccelerate,"Down")
turtle.listen()
game = Game()
game.draw_border()
game.show_status()
while True:
    player.move()
    enemy.move()
    turtle.update()
    # Check for collision between player and fruit
    if player.is_collision(fruit):
        fruit.spawn_fruit()
        game.score += 1
        game.show_status()
        player.size += 1
        player.increase_size()
    if player.is_collision(enemy):
            game.lives -= 1
            game.score -= 2
            if game.lives < -10:
                   print("game over")
                   turtle.bye()
                   break
            if game.lives < 1:
                   print("game over")
                   turtle.bye()
                   break
#turtle.done()
