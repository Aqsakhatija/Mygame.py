# define a function called peri() that accepts radius as a parameter.peri() will calculate the perimeter of a circle, using default radius of 1 unit
#the calling program should called the function twice (a)peri()and (b) peri(9)
import math 
def peri(r=1):
    2*(math.pi)*r
    return 2*math.pi*r
print (peri())
print (peri(9))

