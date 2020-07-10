# Snake game in Python

import turtle
import time
import random

# Creating a delay
delay = 0.1

# Setting up the scores
score = 0
high_score = 0

# Setting up the screen
# Window object
window = turtle.Screen()
# Changing the title of the window
window.title('Snake Game by Aly B')
# Changing the background color of the Screen
window.bgcolor('black')
# Setting up the window sizes.
window.setup(width = 600, height = 600)
# Removing animation
window.tracer(0) # Turns of the screen Updates

# Creating the snakehead
# Setting up the head
snakehead = turtle.Turtle()
# Animation speed
snakehead.speed(0)
# Giving it a shape
snakehead.shape('square')
# Giving a color to the snakehead
snakehead.color('red')
# No drawing so
snakehead.penup()
# Head starts off from the middle
snakehead.goto(0,0)
# Direction of snake head
snakehead.direction = 'up'


# Defining our snake food - code similar to above
snakefood = turtle.Turtle()
snakefood.speed(0)
snakefood.shape('circle')
snakefood.color('grey')
snakefood.penup()
snakefood.goto(0,100)

# Creating a list for segments to increase the size of the snake
segments = []

# Creating a turtle as pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align = 'center', font = ('Courier', 24, 'normal'))

# Defining our moving functions
# Telling snake what to do when button is pressed
def go_up():
    if snakehead.direction != 'down':
        snakehead.direction = 'up'
# Telling snake what to do when button is pressed
def go_down():
    if snakehead.direction != 'up':
        snakehead.direction = 'down'
# Telling snake what to do when button is pressed
def go_right():
    if snakehead.direction != 'left':
        snakehead.direction = 'right'
# Telling snake what to do when button is pressed
def go_left():
    if snakehead.direction != 'right':
        snakehead.direction = 'left'


# Let's now define a function for user moving
def move():
    # Tells the snake to move up  when user indicates by 10 blocks
    if snakehead.direction == 'up':
        y = snakehead.ycor()
        snakehead.sety(y + 15)

    # Tells the snake to move down when user indicates by 10 blocks
    if snakehead.direction == 'down':
        y = snakehead.ycor()
        snakehead.sety(y - 15)

    # Tells the snake to move left when user indicates by 10 blocks
    if snakehead.direction == 'left':
        x = snakehead.xcor()
        snakehead.setx(x - 15)

    # Tells the snake to move right when user indicates by 10 blocks
    if snakehead.direction == 'right':
        x = snakehead.xcor()
        snakehead.setx(x + 15)

# To get the user's keyboard inputs
window.listen() # Letting the window listen to user
window.onkeypress(go_up, 'Up') # Based on what the user inputs
window.onkeypress(go_down, 'Down')
window.onkeypress(go_left, 'Left')
window.onkeypress(go_right, 'Right')

# Creating a loop for the game to run
while True:
    # Updates the window in real time
    window.update()

    # BORDER COLLISION - Checking for a collision with the border
    # The following are conditions if snake goes out of border
    if snakehead.xcor() > 290 or snakehead.xcor() < -290 or snakehead.ycor() > 290 or snakehead.ycor() < -290:
        time.sleep(1) # Delays for 1 sec to restart
        snakehead.goto(0,0) # Sends snake back to 0,0
        snakehead.direction = 'stop'

        # Hide the old segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments list
        segments.clear()

        # increasing the score
        score = 0

        # Resets the Delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align = 'center', font = ('Courier', 24, 'normal'))


    # For snakehead distance to food, every pixel is 20*20
    # Checking for a collision with the food
    if snakehead.distance(snakefood) < 20:
        # Starts food at a random point - Frame size is 300*300
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        # Moves the food around
        snakefood.goto(x,y)
        # Move the food to a random spot

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

        # Reducing delay time
        delay -= 0.005

        # Setting the score to increase by 10
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align = 'center', font = ('Courier', 24, 'normal'))

    # Move the end segments in a reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)

    # Moving the segment 0 to where the head is
    if len(segments) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        segments[0].goto(x,y)


    # Uses the function above
    move()

    # For body collision
    # Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(snakehead) < 20:
            time.sleep(1)
            snakehead.goto(0,0)
            snakehead.direction = 'stop'

            # Hide the segments
            for segment in segments:
                segment.goto(1000,1000)

    #         # Clear the segment and start over
            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Sets the delay by 0.1
    time.sleep(delay)


# Ensures the window runs in a loop
window.mainloop()
