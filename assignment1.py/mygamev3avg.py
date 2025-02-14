import random 
player1roll1= random.randint(1,6)
player1roll2=random.randint(1,6)
player2roll1=random.randint(1,6)
player2roll2=random.randint(1,6)
player3roll1=random.randint(1,6)
player3roll2=random.randint(1,6)
player1total=(player1roll1+player1roll2)
player2total=(player2roll1+player2roll2)
player3total=(player3roll1+player3roll2)
print ("player1total is : ",player1total)
print ("player2total : ", player2total)
print ("player3total is: ", player3total)
highestscore= max(player1total,player2total,player3total)
print("highestscore is : ", highestscore)
average1=(player1total+player2total+player3total)/3 #average using '/' operator 
average2= (player1total+player2total+player3total)//3 #average using '/' operator
print ("average1 '/' is : ", average1)
print ("average2 '//' is: ", average2)