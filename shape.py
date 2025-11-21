import turtle as t
import math as m

def draw_circle(turtle, colour, x, y, radius):
    turtle.penup()
    turtle.color(colour)
    turtle.fillcolor(colour)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.getscreen().update()
    
def draw_rectangle(turtle, colour, x, y, width, height):
    turtle.hideturtle()
    turtle.penup()
    turtle.color(colour)
    turtle.fillcolor(colour)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    
    turtle.end_fill()
    turtle.setheading(0)
    turtle.getscreen().update()
    
def draw_icing(turtle, colour, y):
    turtle.penup()
    turtle.color(colour)
    turtle.fillcolor(colour)
    turtle.goto(-125, y+10)
    turtle.pendown()
    turtle.begin_fill()
    
    for x in range(-125, 125):
        turtle.goto(x, y -10 -10 *m.cos((x/100)*2*m.pi))
    
    turtle.goto(125, y+10)
    turtle.goto(-125, y+10)
    turtle.end_fill()
    turtle.getscreen().update()   
    