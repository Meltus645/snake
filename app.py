import turtle
import time
import random

# moms farm

farm =turtle.Screen()
farm.title("Snake Game")
farm.setup(width=700, height=700) # not as small though
#farm.tracer(0)
turtle.bgcolor('green')

# turtle
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('red')
turtle.forward(600)
turtle.right(90)
turtle.forward(500) 
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()

# Snake
snake =turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('black')
snake.penup()
snake.goto(0,0)
snake.direction ='stop'

# fruit (rodents of course)
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30,30)

#score
old_fruit=[]

scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :",align="center",font=("Courier",24,"bold")