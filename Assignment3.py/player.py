import random

class Player:
    def __init__(self):
        self.score=0  #Initializes player score to 0 
    def roll(self):
        return random.randint(1,6) #Retruns a random value between 1 to 6 