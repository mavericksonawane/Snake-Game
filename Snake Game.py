# SAPACHA KHEL BY MAYUR SONAWANE


import turtle
import time
import random

delay =0.1

#score
score = 0
high_score = 0

# setting up the screen
wn = turtle.Screen()
wn.title("Sapacha Khel by @MAV")
wn.bgcolor("black")
wn.setup(width=1200, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0) #animation speed
head.shape("circle")
head.color("white")
head.penup() # does not draw lines
head.goto(0,0) # Starting position at centre of the screen i.e X , Y coordinates
head.direction = "stop" # Starting in the middle

# Sapache J1
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("red")
food.penup() # does not draw lines
food.goto(0,100) # Starting position at the screen i.e X , Y coordinates

segments = []

#Noting the score and high score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))




# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20) #moving speed

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20) #moving speed

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20) #moving speed

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20) #moving speed

# Keyboard keys
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# MAin game loop
while True:
    wn.update() #update the screen

    # Marnar kasa saap
    if head.xcor()>580 or head.xcor()<-580 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segment list
        segments.clear()

        # Reset the score at new game
        score = 0

        # Reset the delay at the new game
        delay = 0.1

        pen.clear() #clears the screen
        pen.write("Score: {} High Score: {}". format(score, high_score), align="center", font=("courier", 24, "normal"))



    # Food and Snake collision
    if head.distance(food) < 20:
        #Moving food to random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

            # Adding a segment
        new_segment = turtle.Turtle()
        new_segment.speed()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -=0.010

        #Counting the score
        score += 10


        if score > high_score:
            high_score = score

        pen.clear() #clears the screen
        pen.write("Score: {} High Score: {}". format(score, high_score), align="center", font=("courier", 24, "normal"))

    #Move the end segment first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)




    move()

    #Body to Body Collisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segment list
            segments.clear()

            # Reset the score at new game
            score = 0

            # Reset the delay
            delay = 0.1
            pen.clear()  # clears the screen
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",font=("courier", 24, "normal"))

    time.sleep(delay)


wn.mainloop()
