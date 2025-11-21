import turtle
from shape import *
from turtle import *
y= -100

cake_pen = Turtle()
cake_pen.hideturtle()
cake_pen.speed(0)

candle_pen = Turtle()
candle_pen.hideturtle()
candle_pen.speed(0)

screen = turtle.Screen()
screen.setup(width= 600, height=400)
screen.bgcolor("#FFFDD0")
screen.title("Happy Birthday Hsiu Yin!")

pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-250, 50)
pen.pendown()
pen.color("#2e2188")
pen.pensize(5)

def write_message(message, x, y, size=24, colour="#2e2188"):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(colour)
    pen.write(message, align="center", font=("Arial", size, "bold"))

ingredients = {}
ingredients["MaximumBluePurple"]= "#A8AFED"
ingredients["LavenderBlue1"]="#D1D8FF"
ingredients["Lavender1"]="#DEE6FC"
ingredients["MistyBlue"]="#B5C7EB"
ingredients["LavenderBlue2"]="#ccccff"
ingredients["Lavender2"]="#e6e6fa"
ingredients["LightBlue"]="#ADD8E6"
ingredients["cherryred"]="#C30000"
ingredients["candleyellow"]="#FFEF12"

layers =[]
layers.append(["LavenderBlue1", 30])
layers.append(["LavenderBlue2", 20])
layers.append(["Lavender1", 60])
layers.append(["MistyBlue", 40])

# draw plate
draw_rectangle(cake_pen, "#964B00", -150, 230, 300, 20)

for layer in layers:
    draw_rectangle(cake_pen, ingredients[layer[0]], -120,  y, 240, layer[1])
    y+= layer[1]
    
draw_icing(cake_pen, ingredients["Lavender2"], y)

# draw cherries
draw_circle(cake_pen, ingredients["cherryred"], 0, y+10, 10)

# draw candles
draw_circle(candle_pen, ingredients["candleyellow"], 40, y+10, 10)
draw_circle(candle_pen, ingredients["candleyellow"], 80, y+10, 10)

draw_circle(candle_pen, ingredients["candleyellow"], -40, y+10, 10)
draw_circle(candle_pen, ingredients["candleyellow"], -80, y+10, 10)
candle_pen.getscreen().update()

write_message("Happy Birthday Friend Name!", 0, 120, size=30, colour="#2e2188")

cake_pen.getscreen().update()
turtle.done()