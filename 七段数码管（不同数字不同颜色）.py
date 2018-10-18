import turtle, datetime
def drawLine(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    for i in date:
        if i=='0':
            turtle.pencolor("red")
        if i=='1':
            turtle.pencolor("blue")
        if i=='2':
            turtle.pencolor("black")
        if i=='3':
            turtle.pencolor("grey")
        if i=='4':
            turtle.pencolor("darkgreen")
        if i=='5':
            turtle.pencolor("gold")
        if i=='6':
            turtle.pencolor("purple")
        if i=='7':
            turtle.pencolor("violet")
        if i=='8':
            turtle.pencolor("pink")
        if i=='9':
            turtle.pencolor("orange")
        drawDigit(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y%m%d'))
    turtle.hideturtle()
main()
