import turtle
from random import*
from mydesign import*

bob=turtle.Turtle()
bob.speed(100)


for n in range(60):
    bob.penup()
    x = randint(-400,400) 
    y = randint(-400,400)
    bob.goto(x,y)
    bob.pendown()
 
for i in range(6*3):
    circle_size = randint(10, 40)
    bob.pensize(randint(1, 5))
    red_amount   = randint( 0,  30) / 100.0
    blue_amount  = randint(50, 100) / 100.0
    green_amount = randint( 0,  30) / 100.0
    bob.pencolor((red_amount, green_amount, blue_amount))
    bob.circle(circle_size)
    bob .left(60)
    bob.penup()
    x = randint(-400,400) 
    y = randint(-400,400)
    bob.goto(x,y)
    bob.pendown()
    bob.circle(circle_size)
    bob .left(60)
    bob.penup()
    x = randint(-400,400) 
    y = randint(-400,400)
    bob.goto(x,y)
    bob.pendown()
    bob.circle(circle_size)
    bob .left(60)
    bob.penup()
    x = randint(-400,400) 
    y = randint(-400,400)
    bob.goto(x,y)
    bob.pendown() 
    bob.circle(circle_size)
    bob .left(60)
    bob.circle(circle_size)
    bob .left(60)

    
for s in range(30):
    x = randint(-400,400) 
    y = randint(-400,400)
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    star(bob,45)
    bob.color("yellow")
            

