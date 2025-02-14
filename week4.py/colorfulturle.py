import turtle
growing=turtle.Turtle()
sc=turtle.Screen()
sc.screensize(400,400)
x = -10
y = -10
disp=20
sc.bgcolor('black')
colorlist=["red","blue","purple","orange","yellow","indigo","grey","pink","cyan","white",""]
for c in colorlist:
    growing.pencolor(c)
    growing.penup()
    growing.goto(x,y)
    growing.pendown()
    for i in range(4):
     growing.forward(disp)
     growing.left(90)
    disp+=50
    x-=20
    y-=20
sc.exitonclick()
