import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("chocolate")

width = 0  # Starting width of the rectangle
height = 0  # Starting height of the rectangle
t.speed(0)
t.penup()
t.goto(-970, 530)  # Start from the top-left corner
t.pendown()
t.fillcolor("chocolate")
t.shape("turtle")


while True:
    for _ in range(2):  # Draw two pairs of sides for the rectangle
        t.forward(width)  # Move forward by the width
        t.right(90)  # Turn 90 degrees
        t.forward(height)  # Move forward by the height
        t.right(90)  # Turn 90 degrees again
    width += 10  # Increase the width of the rectangle
    height += 5  # Increase the height of the rectangle (slower growth)
    
    if width > 2000:  # Stop once the width reaches a certain size
        break

t.hideturtle()
turtle.done()
