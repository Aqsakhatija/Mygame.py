from Door import Door
from Window import window
class Classroom:
    #all of my class will have one door and 2 windows
    no_of_door=1
    no_of_windows=2
    def __init__(self,l,w,h):
        self.length=l
        self.width=w
        self.height=h
        d1=Door()
        w1=window()
        w2=window()
    def set_dim(self,l,w,h):
        #mutator method or self method
        self.length=l
        self.width=w
        self.height=h
    def get_dim(self):
        #accessor method or get method
        return(self.length, self.width, self.height)
g303= Classroom(1,1,1)
g303.set_dim(2,4,5)
print(g303.get_dim())


       
    
