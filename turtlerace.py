import time
import turtle
from turtle import Turtle
from random import randint

#window setup
window=turtle.Screen()
window.title("TURTLE RACE")
turtle.bgcolor("forestgreen")
turtle.color("black")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("TURTLE RACE",font=("Arial",30,"bold"))

#dirt
turtle.setpos(-400,-180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#finish line
stamp_size=20
square_size=15
finish_line=200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line,(150 - (i*square_size * 2)))
    turtle.stamp()
for j in range(10):
    turtle.setpos(finish_line+square_size,(150-square_size)-(j*square_size*2))
    turtle.stamp()

#turtle1
t1=Turtle()
t1.speed(0)
t1.color('black')
t1.shape('turtle')
t1.penup()
t1.goto(-250,100)
t1.pendown()

#turtle2
t2=Turtle()
t2.speed(0)
t2.color('yellow')
t2.shape('turtle')
t2.penup()
t2.goto(-250,50)
t2.pendown()

#turtle3
t3=Turtle()
t3.speed(0)
t3.color('pink')
t3.shape('turtle')
t3.penup()
t3.goto(-250,0)
t3.pendown()

#turtle4
t4=Turtle()
t4.speed(0)
t4.color('blue')
t4.shape('turtle')
t4.penup()
t4.goto(-250,-50)
t4.pendown()

#turtle5
t5=Turtle()
t5.speed(0)
t5.color('white')
t5.shape('turtle')
t5.penup()
t5.goto(-250,-100)
t5.pendown()

time.sleep(5)#waits 5 seconds before starting the race

#start race noww
for i in range(150):
    t1.forward(randint(1,5))
    t2.forward(randint(1,5))
    t3.forward(randint(1,5))
    t4.forward(randint(1,5))
    t5.forward(randint(1,5))

turtle.exitonclick()
