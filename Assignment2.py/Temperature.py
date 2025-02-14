import random
temper=random.randint(1,400)
print("temperature:",temper)
if (temper>100):
    print ("temperature above boiling point")
    if(temper>320):
        print("temperature above smoke point")
else:
    print("temperature not very high")