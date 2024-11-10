import turtle
import time
import random
delay = 0.1
score = 0
highscore=0
wn=turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("red")
wn.setup(width=799, height=801)
wn.tracer(0)

#paddle1
paddle=turtle.Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=3, stretch_len=1)
paddle.color("green")
paddle.penup()
paddle.goto(-600,0)

#paddl2, goto of ths on right side
paddle2=turtle.Turtle()
paddle2.shape("square")
paddle2.shapesize(stretch_wid=3,stretch_len=1)
paddle2.color("green")
paddle2.penup()
paddle2.goto(600,0)



#ball : circle, goto will be in middle
ball=turtle.Turtle()
ball.shape("circle")
ball.shapesize(stretch_wid=1.99)
ball.color("green")
ball.penup()
ball.goto(0,1)

score1=turtle.Turtle()
score1.color("black")
score1.penup()
score1.goto(-300,300)
score1.hideturtle()
score1.write("Player1Score",font=("Cedarville Cursive",20))

score2=turtle.Turtle()
score2.color("black")
score2.penup()
score2.goto(200,300)
score2.hideturtle()
score2.write("Player1Score",font=("Cedarville Cursive",20))
player1score=0
player2score=0
def goup1():
  y=paddle.ycor()
  y=y+10
  paddle.sety(y)

def godown1():
  y=paddle.ycor()
  y=y-10
  paddle.sety(y)
  
def goup2():
  y=paddle2.ycor()
  y=y+10
  paddle2.sety(y)

def godown2():
  y=paddle2.ycor()
  y=y-10
  paddle2.sety(y)
wn.listen()
wn.onkeypress(goup1,"w")
wn.onkeypress(godown1,"s")


wn.onkeypress(goup2,"Up")
wn.onkeypress(godown2,"Down")
#speed
ball.dx=0.5
ball.dy=-0.5

while True:
  wn.update()
  # move the ball by giving some s[eed tp it.]. we will change x and y using setx and sety and in current ppoistion we will give speed. current positio  is xcor() and ycor() inw hcih we will add speed
  ball.setx(ball.xcor()+ball.dx)
  ball.sety(ball.ycor()+ball.dy)
  #bounce teh ball back from walls. if player crosses left side that means less than -800 then we will make ball come to the middle and change teh speed. increase the score and update on screen too , sam ething we will do for right,up  and down . in this way ball can bounceoff from walls
  #take half of width and height
  if ball.xcor()<-750:
    ball.goto(0, 0)
    ball.dx*=-1
    player2score+=1
    score2.clear()
    score2.write("Player2Score {}".format(player2score),font=("Cedarville Cursive",20))
  if ball.xcor()>750:
    ball.goto(0, 0)
    ball.dx*=-1
    player1score+=1
    score1.clear()
    score1.write("Player1Score {}".format(player1score),font=("Cedarville Cursive",20))
  if ball.ycor()<-500:
    ball.sety(-500)
    ball.dy*=-1
  if ball.ycor()>500:
    ball.sety(500)
    ball.dy*=-1
  #ball bounceoff with paddle. here we will use distnace function id distance between bal, and paddle is less then change the speed of the ball 
  if ball.distance(paddle)<40 and ball.xcor()<-500:
    ball.setx(-500)
    ball.dx*=-1
    ball.dy*=-1
  if ball.distance(paddle2)<40 and ball.xcor()>500:
    ball.setx(500)
    ball.dx*=-1
    ball.dy*=-1