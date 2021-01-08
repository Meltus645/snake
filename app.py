import turtle
import time
import random

# moms farm

farm =turtle.Screen()
farm.title("Snake Game")
farm.setup(width=700, height=700) # not as small though
farm.tracer(0)
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
