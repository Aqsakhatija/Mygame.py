class Myshapes:
    def __init__(self,no_of_sides):
        self.no_of_sides= no_of_sides
    def area(self):
        pass
class Myrect(Myshapes):
    def __init__(self,l,w,n):
        super().__init__(n)
        self.length=l
        self.width=w
    def area (self):
        return(self.length*self.width)
r1=Myrect(4,3,4)
print(r1.area())
        
        