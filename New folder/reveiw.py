#Step 1 Import turle
#Step 2 Use title func and screensize to give screensize
#Step 3 Create turtles for each and everything in the game. For example if we have a player then we have to create a turtle for that.
#T=Turtle.turtle
#Step 4 Use while loop so the game keeps on going. Also use update so the game gets updated.\
import turtle
screen=turtle.Screen()
screen.title("Turtle Game")
screen.bgcolor("green")
T=turtle.Turtle()
#Step 5 We can use forward function to move left and right to change the direction.
#Step 6 In order to move the turtle with WASD we use listen func and keydown.
T.forward(41)
T.right(89)

#if we dont want to draw anything then simply dont use forward(0 and right create turtle and leave it). When we create game we do not use forward() and right() to move.

snake1=Turtle.turtle()
#set poistion using goto()
snake1.goto(200, 200)
snake.shape("square")
snake.color("green")

#Remember mutiple players are there so multiple turtle can be created.
#movement of these things using keydown
def up():
    y=snake1.ycor() #ycor(0 and ycor(0 gives current position
    y=y-10 # speed
    snake1.sety(y) # sety is used to update the value.
def down():
    y=snake1.ycor() #ycor(0 and ycor(0 gives current position
    y=y+10 # speed
    snake1.sety(y) # sety is used to update the value.
def left():
    x=snake1.xcor() #xcor(0 and ycor(0 gives current position
    x=x-10 # speed
    snake1.setx(x) # setx is used to update the value.
def right():
    x=snake1.xcor() #xcor(0 and ycor(0 gives current position
    x=x+10 # speed
    snake1.setx(x) # setx is used to update the value.
#First listen and use keydown and call function
screen.listen()
snake1.keyDown("a", left)
snake1.keyDown("d", right)
snake1.keyDown('w', up)
snake1.keyDown("s", down)

enemy=Turtle.turle()
enemy.shape('square')

score=0

#Remember to display any text like score, gameover we create turtle
score=Turtle.turle()
score.shape("circle")
score.hideturtle()
#write(0 is used to giev text in turtle)
score.write("Score :"+str(score), 10, 10) 

gameover=Turtle.turtle()
gameover.shape("circle")
gameover.hideturtle()
gameover.write("Gameover", 100,100)

while True:
    screen.update()
    #For collide we use distance()
    if snake1.distance(enemy) <10:
        score+=1

#Step 7 To give the text on the screen we create a turtle and use the write func to display the text on the screen.
#Step 8 create functions for the movement whenever we make the x negative, x positive is right, y negative is up, and y positive is down.
#Also use xcor and ycor and that only you add and subtract to the current pos of the player.
#ex. T.xcor() + 20
#This means we are adding 20 to x to go to the right and if you add -20 to x you goo left, viceversa for the ycor.
#Step 9 One inbuilt func that checks the touch or collision bewtween 2 is .distance.
#ex. T.distance(T2) < 10

#-----------------------------------------------Assignment-------------------------------------------
#create a seperate file hoemwork and create shapes like square, circle, rectangle.





















