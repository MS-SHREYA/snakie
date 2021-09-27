
import turtle
import random
import time

# creating a screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.tracer(0)
screen.setup (width = 400, height = 360)
screen.bgcolor("green")

# creating border
turtle.speed(4)
turtle.pensize(3)
turtle.penup()
turtle.goto(-150,150)
turtle.pendown()
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.penup()
turtle.hideturtle()

# creating snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('triangle')
snake.color('blue')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop' # to stop moving after coming to 0,0

# creating food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('orange')
food.penup()
food.goto(30,30)

# creating score text
score = turtle.Turtle()
score.speed(0)
score.color('black')
score.penup()
score.goto(0,300)
score.write('SCORE : ', align = 'center', font = ('calibri', 16, 'bold'))

# defining snake movement
def snake_go_up():
    if snake.direction != 'down':
        snake.direction = 'up'
def snake_go_right():
    if snake.direction != 'left' : 
        snake.direction = 'right'
def snake_go_down():
    if snake.direction != 'up' : 
        snake.direction = 'down'
def snake_go_left():
    if snake.direction != 'right' : 
        snake.direction = 'left'
def snake_move():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x+20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x-20)

screen.listen() # listen = listens to our key presses
screen.onkeypress(snake_go_up, 'Up')
screen.onkeypress(snake_go_down, 'Down')
screen.onkeypress(snake_go_left, 'Left')
screen.onkeypress(snake_go_right, 'Right')