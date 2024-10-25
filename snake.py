import turtle
import time
import random
import pygame


#okno
window = turtle.Screen()
window.title("Hadik")
window.bgcolor("#266EA5")
window.setup(width = 600, height=600)

#had
snake = turtle.Turtle()
snake.shape("turtle")
snake.color("#3C5F2A")
snake.goto(0,0)
snake.penup()
snake.speed(0)

#jidlo
food = turtle.Turtle()
window.tracer(0)
food.shape("circle")
food.color("#272D2B")
food.penup()
food.goto(200,200)

#score
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,250)
pen.color("white")
pen.write(f"Skore: {score}", align="center", font=("calibri",24,"bold"))

#pohyb
def up():
    snake.setheading(90)

def down():
    snake.setheading(270)

def left():
    snake.setheading(180)

def right():
    snake.setheading(0)

def move():
    snake.forward(20)

pygame.mixer.init()

def play_sound():
    pygame.mixer.music.load("eatingsoundCut.wav")
    pygame.mixer.music.play()

window.listen()
window.onkeypress(up,"Up")
window.onkeypress(down,"Down")
window.onkeypress(left,"Left")
window.onkeypress(right,"Right")

#hlavni cyklus
while True: 
    window.update()

    # kontrola ohraniceni
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        score = 0
        time.sleep(1)
        snake.goto(0,0)
        window.tracer(0)
        pen.clear()
        pen.write(f"Skore: {score}", align="center", font=("calibri",24,"bold"))
        window.bgpic("nopic")
        window.bgcolor("#266EA5")
        snake.shape("turtle")
        snake.color("#3C5F2A")

    # kontrola snezeni jidla
    if snake.distance(food) < 20:
        window.tracer(0)
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x, y)
        play_sound()
        score += 1
        pen.clear()
        pen.write(f"Skore: {score}", align="center", font=("calibri",24,"bold"))

        #zmena barvy veci podle skore
        if score > 14:
            turtle.register_shape("turtleTiny45.gif")
            snake.shape("turtleTiny45.gif")
            window.bgpic("space.png")
            food.color("#E9E6E6")
            pen.write(f"Skore: {score}", align="center", font=("calibri",24,"bold"))

        elif score % 2 != 0:
            snake.color("#9DAF94")

        else:
            snake.color("#3C5F2A")
        
    move()

    # zmena rychlosti podle skore
    speed = 0.1 - (score * 0.002)
    time.sleep(speed)



