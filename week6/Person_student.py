class Person:
    def __init__(self,n,id,age):
        self.name=n
        self.id=id
        self.age=age
class student(Person):
    def __init__(self,n,id,age,prog):
        super().__init__(n,id,age) ##calling the parent class init method
        self.prog=prog
s1=student("joe",5699,29,"computerscience")
print (s1.student)
