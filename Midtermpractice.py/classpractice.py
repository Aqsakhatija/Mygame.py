class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for marks in self.marks:
            sum +=marks
        print ("hi", self.name, "your avg marks is: ",sum/3)




s1= Student("jennifer", [95,78,89])
s1.get_avg()