import turtle
turtle.setup(500,500,-200,-200)
s=5
turtle.penup()
for i in range(25):
    turtle.fd(s)
    turtle.pendown()
    turtle.left(90)

    turtle.fd(s)
    turtle.left(90)
    
    s=s+5
    
    turtle.fd(s)
    turtle.left(90)
    
    turtle.fd(s)
    turtle.left(90)
    
    s=s+5
  
