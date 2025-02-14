class RectangleClass:
    # rectangle has length and width which is different for each object 
    totalRectangles=0

    def __init__(self):
        RectangleClass.totalRectangles +=1
    def setDim(self,l,b):
        self.length=l
        self.width=b

    def peri(self):
        return(2*self.length+2*self.width)
    def area(self):
        a=(self.length*self.width)
        return a
r1=RectangleClass()
r1.setDim(6,9)
print("length of my rectangle is: " ,r1.length)
print("width of my rectangle is: ",r1.width)

