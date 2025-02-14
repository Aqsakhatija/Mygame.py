import turtle
red_turtle=turtle.Turtle()
blue_turtle=turtle.Turtle()
sc=turtle.Screen()
sc.bgcolor('black')
sc.screensize(400,400)
red_turtle.shape('turtle')
blue_turtle.shape('turtle')
red_turtle.pencolor('green')
blue_turtle.pencolor('yellow')
blue_turtle.goto(100,100)
blue_turtle.penup()
alist=[0,1,2,3]
for items in alist:
    blue_turtle.forward(100)
    blue_turtle.left(90)
for items in alist:
    red_turtle.forward(200)
    red_turtle.left(90)
    sc.exitonclick()