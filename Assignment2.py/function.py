import math 
def avg(numbers):
    return sum(numbers)/len(numbers)
def sumsqdiff(numbers,avg):
    ssd=0
    for num in numbers:
        ssd+=(num-avg)**2
    return ssd 
numbers=[2,4,6,8,10,12,14,16,18,20]
avg=avg(numbers)
ssd=sumsqdiff(numbers,avg)
standard_deviation=math.sqrt(ssd/len(numbers))
print ("the standard deviation: ",standard_deviation)