import turtle
# setup the screen 
sc = turtle.Screen()
sc.screensize(400,400)
sc.bgcolor('black')
#create the turtle
growing= turtle.Turtle()
#initialize variables
x= 0
y = -10
disp = 20 #initial circle radius
#define colors
colorlist=["red","blue","purple","orange","yellow","indigo","grey","pink","cyan","white"]
# draw circles to create sphere illusion
for color in colorlist:
    growing.pencolor(color)
    growing.penup()
    growing.goto(x,y -disp)
    growing.pendown()
    growing.circle(disp) # drwa circle

    disp += 20  #increase circle size

sc.exitonclick()