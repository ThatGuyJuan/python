import turtle
import math
import random 


twin = turtle.Screen()
twin.clear()
t = turtle.Turtle()
#tWin = turtle.Screen()
t.penup()
t.goto(100,0)
t.pendown()   
t.color("#ff0000")
t.width(5)
t.goto(0,100)
t.goto(-100,0)
t.goto(0,-100)
t.goto(100,0)
t.goto(0,100)
t.color("#0048BA")
t.width(5)
t.goto(-65,65)
t.goto(-100,0)
t.goto(-65,-65)
t.goto(0,-100)
t.goto(65,-65)
t.goto(100,0)
t.goto(65,65)
t.goto(0,100)
twin.exitonclick()

