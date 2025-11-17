import turtle
import math

Size=50
Xscale=5
Yscale=20
Step=1

# Set up the screen
window = turtle.Screen()
window.bgcolor("White")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

for x in range(1,2*Size,Step):
    y=math.log(x)
    pen.goto(Xscale*x,Yscale*y)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()