import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(78)
h = 0.001
n = 219
for i in range(567):
    c = colorsys.hsv_to_rgb(h,1,.7)
    h += 1/n
    t.up()
    t.goto(-8,25)
    t.down()
    t.pencolor('black')
    t.pensize(4)
    t.fd(18)
    t.rt(40)
    t.fillcolor(c)
    t.begin_fill()
    t.pensize(9)
    t.fd(i)
    t.circle(i,24)
    t.end_fill()
    t.lt(65)
    t.fd(i)
    t.fillcolor(c)
    t.begin_fill()
    t.circle(i,60,steps=15)
    t.end_fill()
t.done()
