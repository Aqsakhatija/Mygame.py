import turtle 
#Setup screen
sc = turtle.Screen()
sc.screensize(400,400)
sc.bgcolor('black')
# Create the turtle
growing= turtle.Turtle()
#Initialize variables
x = -10 
y = -10
disp = 20
# Define colors
colorlist= ["red","blue","purple","orange","yellow","indigo","grey","pink","cyan","white"]
# Draw squares to create 3D illusion
for color in colorlist:
    growing.pencolor(color) 
    growing.penup()
    growing.goto(x,y)
    growing.pendown()

    for i in range(4): #Draw square
        growing.forward(disp)
        growing.left(90)
    
    disp += 50 #increase sqaure size
    x -= 20 # adjust position to centre next square
    y -=20

sc.exitonclick()




