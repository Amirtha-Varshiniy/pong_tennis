import turtle
ground=turtle.Screen()
ground.bgpic("ground.png")
ground.addshape("ball.gif")
ground.addshape("left player.gif")
ground.addshape("right player.gif")

rplayer=turtle.Turtle()
rplayer.penup()
rplayer.shape("right player.gif")
rplayer.goto(400,-200)

lplayer=turtle.Turtle()
lplayer.penup()
lplayer.shape("left player.gif")
lplayer.goto(-400,200)

ball=turtle.Turtle()
ball.penup()
ball.shape("ball.gif")

rscore=turtle.Turtle()
rscore.hideturtle()
rscore.penup()
rscore.goto(100,250)
rscore.color("white")
rscore.write("Rightplayer Score: 0",font=("Courier",20,"bold"))

lscore=turtle.Turtle()
lscore.hideturtle()
lscore.penup()
lscore.goto(-400,250)
lscore.color("white")
lscore.write("Leftplayer: 0",font=("Courier",20,"bold"))

def lup():
    y=lplayer.ycor()
    lplayer.sety(y+10)
def ldown():
    y=lplayer.ycor()
    lplayer.sety(y-10)
def lfront():
    x=lplayer.xcor()
    lplayer.setx(x+10)
def lback():
    x=lplayer.xcor()
    lplayer.setx(x-10)

def rup():
    a=rplayer.ycor()
    rplayer.sety(a+10)
def rdown():
    a=rplayer.ycor()
    rplayer.sety(a-10)
def rfront():
    b=rplayer.xcor()
    rplayer.setx(b+10)
def rback():
    b=rplayer.xcor()
    rplayer.setx(b-10)

turtle.onkeypress(lup,"w")
turtle.onkeypress(ldown,"s")
turtle.onkeypress(lfront,"d")
turtle.onkeypress(lback,"a")
turtle.onkeypress(rup,"Up")
turtle.onkeypress(rdown,"Down")
turtle.onkeypress(rfront,"Right")
turtle.onkeypress(rback,"Left")

turtle.listen()
a=20
b=20
leftscore=0
rightscore=0
while True:
    ground.update()
    x=ball.xcor()
    y=ball.ycor()
    ball.setpos(x+a,y+b)
    if rplayer.distance(ball)<20:
        a=-a
        rightscore+=1
    if lplayer.distance(ball)<20:
        a=-a
        leftscore+=1
    if ball.ycor()<-280:
        b=-b
    if ball.ycor()>280:
        b=-b
    if ball.xcor()<-450:
        rscore.clear()
        rightscore+=1
        rscore.write(("Rightplayer Score: {}").format(rightscore),font=("Courier",20,"bold"))
        ball.goto(0,0)
        
    if ball.xcor()>450:
        lscore.clear()
        leftscore+=1
        lscore.write(("Leftplayer Score:{}").format(leftscore),font=("Courier",20,"bold"))
        ball.goto(0,0)

turtle.done()