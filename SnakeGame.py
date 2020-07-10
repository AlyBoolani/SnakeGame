# Snake game in Python

import turtle
import time
import random

# Creating a delay
delay = 0.1

# Setting up the screen
# Window object
window = turtle.Screen()
# Changing the title of the window
window.title('Snake Game by Aly B')
# Changing the background color of the Screen
window.bgcolor('black')
# Setting up the window sizes.
window.setup(width = 500, height = 500)
# Removing animation
window.tracer(0)

# Creating the snakehead
# Setting up the head
snakehead = turtle.Turtle()
# Animation speed
snakehead.speed(0)
# Giving it a shape
snakehead.shape('triangle')
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
snakefood.shape('square')
snakefood.color('blue')
snakefood.penup()
snakefood.goto(0,100)

# Defining our moving functions
# Telling snake what to do when button is pressed
def go_up():
    snakehead.direction = 'up'
# Telling snake what to do when button is pressed
def go_down():
    snakehead.direction = 'down'
# Telling snake what to do when button is pressed
def go_right():
    snakehead.direction = 'right'
# Telling snake what to do when button is pressed
def go_left():
    snakehead.direction = 'left'


# Let's now define a function for user moving
def move():
    # Tells the snake to move up  when user indicates by 10 blocks
    if snakehead.direction == 'up':
        y = snakehead.ycor()
        snakehead.sety(y + 10)

    # Tells the snake to move down when user indicates by 10 blocks
    if snakehead.direction == 'down':
        y = snakehead.ycor()
        snakehead.sety(y - 10)

    # Tells the snake to move left when user indicates by 10 blocks
    if snakehead.direction == 'left':
        x = snakehead.xcor()
        snakehead.setx(x - 10)

    # Tells the snake to move right when user indicates by 10 blocks
    if snakehead.direction == 'right':
        x = snakehead.xcor()
        snakehead.setx(x + 10)

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

    # For snakehead distance to food, every pixel is 20*20
    if snakehead.distance(snakefood) < 20:
        # Starts food at a random point - Frame size is 300*300
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        # Moves the food around
        snakefood.goto(x,y)
        # Move the food to a random spot
    # Uses the function above
    move()
    # Sets the delay by 0.1
    time.sleep(delay)


# Ensures the window runs in a loop
window.mainloop()
