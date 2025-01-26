import random 
player1roll1=random.randint(1,6)
player1roll2=random.randint(1,6)
player2roll1=random.randint(1,6)
player2roll2=random.randint(1,6)
player3roll1=random.randint(1,6)
player3roll2=random.randint(1,6)
player1total=(player1roll1+player1roll2)
player2total=(player2roll1+player2roll2)
player3total=(player3roll1+player3roll2)
print ("player1 rolled: ", player1total)
print ("player2 rolled: ", player2total)
print ("player3 rolled: ", player3total)
highestvalue=max(player1total,player2total,player3total)
print ("highest score is : ", highestvalue)
average1= player1total+player2total+player3total/3 #average using '/' operator without parenthesis
average2=player1total+player2total+player3total//3 #averahe using '//' operator without parenthesis
print ("average1 without parenthesis : ", average1)
print ("average2 without parenthesis :  ", average2)
