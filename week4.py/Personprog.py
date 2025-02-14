class Person:
    breathes = True
    def __init__(self,a,n):
        self.age =a
        self.name =n
    def sethair(self,hc):
        self.hair_color=hc
p2 = Person(22,"Aqsa")    
p2.sethair("golden brown")
print ( "Age of", p2.name ,"is" , p2.age , "and her  hair color is ", p2.hair_color ) 

