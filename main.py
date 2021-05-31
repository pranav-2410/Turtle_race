import turtle as tt
import random as rn

t = tt.Turtle()
wn = tt.Screen()
wn.setup(1300,750)
wn.bgcolor("gold")
s = tt.getscreen()

start:
c = t.clone()
d = t.clone()
t.shape("turtle")
t.pensize(15)
t.shapesize(2, 2, 2)

b = t.clone()
colors = ["red", "blue", "pink", "yellow", "green", "black","white", "orange"]

name1 = tt.textinput("PLAYER 1", "ENTER NAME OF PLAYER 1:")
name2 = tt.textinput("PLAYER 2", "ENTER NAME OF PLAYER 2:")

color1 = tt.textinput("COLOR SELECTION", "Player 1 enter the color you want:")
while color1.lower() not in colors:
    color1 = tt.textinput("WRONG COLOR SELECTED", "Player 1 enter the color you want:")

color2 = tt.textinput("COLOR SELECTION", "Player 2 enter the color you want:")
while color2.lower() not in colors:
    color2 = tt.textinput("WRONG COLOR SELECTED", "Player 2 enter the color you want:")

t.color("cyan", color2) #color2
b.color("violet", color1) #color1

t.penup()
t.goto(300, -300)
t.lt(90)
t.rt(360)
t.pendown()
t.write(name2, align="right", font=("Arial", 25, "bold"))

b.penup()
b.goto(-300, -300)
b.lt(90)
b.lt(360)
b.pendown()
b.write(name1, align="right", font=("Arial", 25, "bold"))

c.penup()
c.pen(pensize=15, pencolor="grey", speed=10)
c.goto(0, 350)
c.pendown()
c.rt(90)
c.fd(700)

d.penup()
d.pen(pensize=15, pencolor="white", speed=10)
d.goto(-500, 200)
d.pendown()
d.fd(900)
d.write("----FINISH LINE----", move=True, align="left", font=("Arial", 25, "bold"))


def mov_2(x, y):
    if y <= 200:
        t.fd(rn.randint(1, 100))
    else:
        t.color("green")
        t.write("I WON :)", align="center", font=("Arial", 30, "bold"))


def mov_1(x, y):
    if y <= 200:
        b.fd(rn.randint(1, 100))
    else:
        b.color("green")
        b.write("I WON :)", align="center", font=("Arial", 30, "bold"))


t.onclick(mov_2)
b.onclick(mov_1)

if t.ycor()>=200 or b.ycor()>=200:
    t.reset()
    b.reset()
    goto start;

tt.done()