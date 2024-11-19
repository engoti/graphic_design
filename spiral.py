import turtle

START_X = -200
START_Y = 0
NUM_LINES = 36
LINE_LENGTH = 400
ANGLE = 170
ANIMATION_SPEED = 0

turtle.hideturtle
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

turtle.speed(ANIMATION_SPEED)

for x in range(NUM_LINES):
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)
    
turtle.hideturtle()
turtle.done()
