import turtle
s= 200
turtle.setup(500,500,-200,-200)

while s > 5:
    t= 90
    turtle.seth(t)
    turtle.fd(s)
    
    t = t - 90
    turtle.seth(t)
    turtle.fd(s)
    
    s = s - 5
    t = t - 90
    turtle.seth(t)
    turtle.fd(s)
    
    t = t - 90
    turtle.seth(t)
    turtle.fd(s)
    
    s= s - 5
