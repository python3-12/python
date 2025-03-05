import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("chocolate")

a = 0  # Starting size of the side of the square
b = 90  # Always turn 90 degrees to form a square
t.speed(0)
t.penup()
t.goto(0, 0)  # Start from top-left corner to form the square
t.pendown()
t.fillcolor("aqua")
t.shape("turtle")
t.shapesize(stretch_len=20, stretch_wid=20)

while True:
    for _ in range(4):  # Draw four sides of a square
        t.forward(a)  # Move forward by the length of a (side of the square)
        t.right(b)  # Turn 90 degrees after each side
    a += 10  # Increase the side length to make the square grow large
    b += 1
    if a > 1100:  # Stop once the square gets big enough
        break

t.hideturtle()
turtle.done()
