#Define a function that finds the median value of three numbers 
def median (x,y,z):
    sorted_list=sorted(list(x,y,z))
    return sorted_list[1]
x=int(input("Enter a number: "))
y=int(input("enter a nuber: "))
z=int(input("enter a number: "))
print(median(x,y,z))

