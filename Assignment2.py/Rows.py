rows=int(input("enter number of rows:"))
for i in range(1,rows+1):
    if i % 2==1:
        print("+"*i)
    else:
        print("-"*i)
