import turtle as t
t.setup(650,350,50,200)
t.penup()
t.goto(-100,-150)
t.pendown()
for i in range(3):
    t.fd(200)
    t.left(120)
t.penup()
t.goto(-50,-(150-50*3**0.5))
t.pendown()
for i in range(3):
    t.fd(100)
    t.left(-120)
t.done()

