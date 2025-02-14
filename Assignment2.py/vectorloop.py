import math
x=int(input("enter first dimension: "))
y=int(input("enter second dimension: "))
z=int(input("enter third dimension: "))
vector=(x,y,z)
sumofsquare=0
for num in range(3):
    sumofsquare+=num**2
magnitude_of_vector=math.sqrt(sumofsquare)
print("magnitude of the vector is: ",magnitude_of_vector)
