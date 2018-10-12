import turtle as t
t.setup(650,350,50,200)
t.penup()
t.goto(-100,-150)
t.seth(90)
t.pendown()
for i in range(3):
    t.fd(300)
    t.right(120)
t.penup()
t.goto(-(50*3**0.5+100),0)
t.seth(-30)
t.pendown()
for i in range(3):
    t.fd(300)
    t.left(120)
t.seth(30)
t.fd(100)
t.done()
