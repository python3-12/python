import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("pink")
t.pencolor("white")
t.pensize("5")

a = 0  # Starting size of the side of the square
b = 15  # Always turn 90 degrees to form a square
t.speed(0)
t.penup()
t.goto(0, 0)  # Start from top-left corner to form the square
t.pendown()
t.fillcolor("aqua")
t.shape("turtle")

while True:
    for _ in range(4):  # Draw four sides of a square
        t.forward(a)  # Move forward by the length of a (side of the square)
        t.right(b)  # Turn 90 degrees after each side
    a += 1  # Increase the side length to make the square grow large
    if a > 10:
        t.color("yellow")
    if a > 20:
        t.color("green")
    if a > 30:
        t.color("red")
    if a > 40:
        t.color("orange")
    if a > 50:
        t.color("blue")
    if a > 60:
        t.color("gray")
    if a > 70:
        t.color("sky blue")
    if a > 80:
        t.color("navy")
    if a > 90:
        t.color("cyan")
    if a > 100:
        t.color("black")
    if a > 105:
        t.color("white")
    if a > 110:
        t.color("yellow")
    if a > 115:
        t.color("red")
    if a > 120:
        t.color("orange")
    if a > 125:
        t.color("blue")
    if a > 130:
        t.color("gray")
    if a > 135:
        t.color("sky blue")
    if a > 140:
        t.color("navy")
    if a > 145:
        t.color("cyan")
    if a > 150:  # Stop once the square gets big enough
        break

t.hideturtle()
turtle.done()
