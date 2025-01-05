import turtle

t = turtle.Turtle()
t.pensize(2)
t.shape("turtle")
turtle.bgcolor("black")

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

t.pencolor("white")

go(-30,-100)
t.seth(93)
t.circle(-110,30)
go(-30,-100)
t.seth(150)
t.forward(10)
t.seth(200)
t.forward(8)
t.seth(150)
t.forward(5)
t.seth(180)
t.forward(8)
t.seth(55)
t.circle(100,30)
t.seth(100)
t.circle(20,60)
t.seth(120)
t.circle(-80,30)
t.forward(50)
print(t.pos())
t.seth(325)
t.circle(200,20)
t.seth(260)
t.forward(12)


go(-64.38,58.73)
t.seth(5)
t.circle(-200,33)
print(t.pos())
t.seth(220)
t.circle(-95,40)
t.seth(263)
t.forward(57)


t.hideturtle()
turtle.done()
