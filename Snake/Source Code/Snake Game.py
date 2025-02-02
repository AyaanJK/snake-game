# Snake Game

import turtle
import time
import random

debounce = 0.1

# Score
score = 0
high_score = 0

win = turtle.Screen()
win.title("Snake Game by @AikonDev")
win.bgcolor("black")
win.setup(width = 600, height = 600)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Collectibles
collectible = turtle.Turtle()
collectible.speed(0)
collectible.shape("square")
collectible.color("green")
collectible.penup()
collectible.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align = "center", font = ("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != 'down':
        head.direction = "up"

def go_down():
    if head.direction != 'up':
        head.direction = "down"

def go_left():
    if head.direction != 'right':
        head.direction = "left"

def go_right():
    if head.direction != 'left':
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def reset_score():
    score = 0
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

def reset_debounce():
    debounce = 0.1

# Keybinds
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# Main Game Loop
while True:
    win.update()

    # Border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.hideturtle()
        
        segments.clear()
        reset_score()
        reset_debounce()

    if head.distance(collectible) < 20:
        # Collectible location randomiser (import random library)
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        collectible.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten debounce
        debounce -= 0.001

        # Increase score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

    # Segment movement
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Segment 0 Movement
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide segments
            for segment in segments:
                segment.hideturtle()
        
            segments.clear()
            reset_score()
            reset_debounce()

    time.sleep(debounce)

win.mainloop()