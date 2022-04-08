#Pong game in android using python.
import turtle

#Creating the screen
sc=turtle.Screen()
sc.bgcolor("black")
sc.title("Pong Game BY TannuMishra")
sc.tracer(0)

right_player=0
left_player=0

#Left_Paddle.
Lp=turtle.Turtle()
Lp.shape("square")
Lp.color("cyan")
Lp.penup()
Lp.shapesize(11,2)
Lp.goto(-980,0)

#Right_Paddle.
Rp=turtle.Turtle()
Rp.shape("square")
Rp.color("cyan")
Rp.penup()
Rp.shapesize(11,2)
Rp.goto(980,0)

#Creating The Ball.
Bl=turtle.Turtle()
Bl.speed(20)
Bl.shape("circle")
Bl.color("red")
Bl.penup()
Bl.shapesize(2,2)
Bl.goto(0,0)
Bl.dx=3.5
Bl.dy=-3.5

#Player_Points or Score.
Ps=turtle.Turtle()
Ps.color("green")
Ps.penup()
Ps.hideturtle()
Ps.goto(0,400)
Ps.write("Left Player:0           Right Player:0",align="center",font=('Courier',10,'normal'))

#Functions To Paddle up.
def paddle1up():
    y=Lp.ycor()
    y+=20
    Lp.sety(y)
def paddle1down():
    y=Lp.ycor()
    y-=20
    Lp.sety(y)
def paddle2up():
    y=Rp.ycor()
    y+=20
    Rp.sety(y)
def paddle2down():
    y=Rp.ycor()
    y-=20                   
    Rp.sety(y)
    
#Keyboard Bindings
sc.listen()
sc.onkeypress(paddle1up,"w")
sc.onkeypress(paddle1down,"s")
sc.onkeypress(paddle2up,"Up")
sc.onkeypress(paddle2down,"Down")

#Game Loop
while True:
    sc.update()
    Bl.setx(Bl.xcor()+Bl.dx)
    Bl.sety(Bl.ycor()+Bl.dy)
    if Bl.ycor()>450:
            Bl.sety(450)
            Bl.dy*=-1
    if Bl.ycor()<-450:
            Bl.sety(-450)
            Bl.dy *= -1
    if Bl.xcor()>1055:
            Bl.goto(0,0)
            Bl.dx*=-1
    if Bl.xcor()<-1060:
            Bl.goto(0,0)
            Bl.dx*=-1
    # Collision with the the walls.            
    if (Bl.xcor()>955 and Bl.xcor()<980) and (Bl.ycor()<Rp.ycor()+40 and Bl.ycor()>Rp.ycor()-40):
            Bl.setx(955)
            Bl.dx*=-1
            right_player+=1
            Ps.clear()
            Ps.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 10, "normal"))
    if (Bl.xcor()<-955 and Bl.xcor()>-780) and (Bl.ycor()<Lp.ycor()+40 and Bl.ycor()>Lp.ycor()-40):
            Bl.setx(-955)
            Bl.dx*=-1
            left_player+=1
            Ps.clear()
            Ps.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 10, "normal"))
   
    





