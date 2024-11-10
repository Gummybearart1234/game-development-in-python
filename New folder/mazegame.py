import turtle

#create screen
screen1=turtle.Screen()
screen1.title("mazegame")
screen1.bgcolor("white")
screen1.screensize(799,901)
#turtle1
t1=turtle.Turtle()
t1.shape("square")
t1.color("black")
t1.shapesize(stretch_wid=0.3, stretch_len=16)
t1.penup()
t1.goto(0, 0)

t2=turtle.Turtle()
t2.shape("square")
t2.color("black")
t2.shapesize(stretch_wid=4, stretch_len=0.3)
t2.penup()
t2.goto(-160, -40)

t3=turtle.Turtle()
t3.shape("square")
t3.color("black")
t3.shapesize(stretch_wid=4, stretch_len=0.3)
t3.penup()
t3.goto(160,-40)

t4=turtle.Turtle()
t4.shape("square")
t4.color("black")
t4.shapesize(stretch_wid=0.3, stretch_len=16)
t4.penup()
t4.goto(0,-240)

t5=turtle.Turtle()
t5.shape("square")
t5.color("black")
t5.shapesize(stretch_wid=4, stretch_len=0.3)
t5.penup()
t5.goto(160,-200)

t6=turtle.Turtle()
t6.shape("square")
t6.color("black")
t6.shapesize(stretch_wid=4, stretch_len=0.3)
t6.penup()
t6.goto(-160,-200)

t7=turtle.Turtle()
t7.shape("square")
t7.color("black")
t7.shapesize(stretch_wid=0.3, stretch_len=4)
t7.penup()
t7.goto(-120,-80)

t8=turtle.Turtle()
t8.shape("square")
t8.color("black")
t8.shapesize(stretch_wid=4, stretch_len=0.3)
t8.penup()
t8.goto(-80,-120)

t9=turtle.Turtle()
t9.shape("square")
t9.color("black")
t9.shapesize(stretch_wid=0.3, stretch_len=4)
t9.penup()
t9.goto(-40,-160)

t10=turtle.Turtle()
t10.shape("square")
t10.color("black")
t10.shapesize(stretch_wid=0.3, stretch_len=4)
t10.penup()
t10.goto(40,-80)

t11=turtle.Turtle()
t11.shape("square")
t11.color("black")
t11.shapesize(stretch_wid=4, stretch_len=0.3)
t11.penup()
t11.goto(80, -40)

t12=turtle.Turtle()
t12.shape("square")
t12.color("black")
t12.shapesize(stretch_wid=0.3, stretch_len=4)
t12.penup()
t12.goto(120,-160)

player=turtle.Turtle()
player.shape("square")
player.color("black")
player.shapesize(stretch_wid=1.1, stretch_len=1.09)
player.penup()
player.goto(-149,-121)

def goup():
  y=player.ycor()
  y=y+20
  player.sety(y)

def godown():
  y=player.ycor()
  y=y-20
  player.sety(y)

def goleft():
  x=player.xcor()
  x=x-20
  player.setx(x)

def goright():
  x=player.xcor()
  x=x+20
  player.setx(x)

screen1.listen()
screen1.onkeypress(goup,"w")
screen1.onkeypress(goleft,"a")
screen1.onkeypress(godown,"s")
screen1.onkeypress(goright,"d")

coin=turtle.Turtle()
coin.shape("circle")
coin.color("black")
coin.shapesize(stretch_wid=1, stretch_len=1)
coin.penup()
coin.goto(100,-140)

coin1=turtle.Turtle()
coin1.shape("circle")
coin1.color("black")
coin1.shapesize(stretch_wid=1, stretch_len=1)
coin1.penup()
coin1.goto(0,-200)

coin2=turtle.Turtle()
coin2.shape("circle")
coin2.color("black")
coin2.shapesize(stretch_wid=1, stretch_len=1)
coin2.penup()
coin2.goto(0,-120)

coin3=turtle.Turtle()
coin3.shape("circle")
coin3.color("black")
coin3.shapesize(stretch_wid=1, stretch_len=1)
coin3.penup()
coin3.goto(-120,-40)
  

score=turtle.Turtle()
score.color("black")
score.penup()
score.goto(-215, 78)
score.write("score",font=("Cedarville Cursive",142))
score1=0
while True:
  screen1.update()
  if player.distance(t1)<19 or player.distance(t2)<19 or player.distance(t3)<19 or player.distance(t4)<19 or player.distance(t5)<19 or player.distance(t6)<19 or player.distance(t7)<19 or player.distance(t8)<19 or player.distance(t9)<19 or player.distance(t10)<19 or player.distance(t11)<19 or player.distance(t12)<19:
    player.goto(-149, -120)

  if player.distance(coin)<21:
    coin.hideturtle()
    coin.goto(900,900)
    score1+=1
    score.clear()
    score.write("score"+str(score1),font=("Cedarville Cursive",142))

  if player.distance(coin1)<21:
    coin1.hideturtle()
    coin1.goto(900,900)
    score1+=1
    score.clear()
    score.write("score"+str(score1),font=("Cedarville Cursive",142))

  if player.distance(coin2)<21:
    coin2.hideturtle()
    coin2.goto(900,900)
    score1+=1
    score.clear()
    score.write("score"+str(score1),font=("Cedarville Cursive",142))

  if player.distance(coin3)<21:
    coin3.hideturtle()
    coin3.goto(900,900)
    score1+=1
    score.clear()
    score.write("score"+str(score1),font=("Cedarville Cursive",142))

