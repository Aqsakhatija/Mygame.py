import random 
from player import Player

class Game:
    def __init__(self):
        self.players= [Player(),Player(),Player()] # Create 3 players
        self.guess= 0 # Initializes guess to 0 
    
    def start(self):
        self.guess = random.randint(1,6) # Generates a random number between 1 to 6

    def match(self):
        for player in self.players:
            if player.roll() == self.guess:
                player.score += 1 
                

         
    
    