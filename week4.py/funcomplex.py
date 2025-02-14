import math 
def mod (a,b):
    return math.sqrt(a**2+b**2)
def difference(x, x1):
    return x-x1
print ("calculating magnitude of a vector between (0,0)and (2,3)")
print (mod(difference (2,0),difference(3,0)))
