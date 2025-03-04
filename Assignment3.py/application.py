from game import Game

class Application:
    def __init__(self):
        self.game= Game()

    def run(self):
        for round_number in range(5):
            print ("/nRound",round_number + 1)
            self.game.start()
            print ("Generated Guess:",self.game.guess)

            for player_index in range(3):
                player = self.game.players[player_index]
                roll_value= player.roll()
                print ("player",player_index + 1,"rolled:",roll_value)
                if roll_value == self.game.guess:
                    player.score += 1 

            print ("Current score:", [player.score for player in self.game.players])
        
        scores= [player.score for player in self.game.players]
        max_score = max(scores)
        winner = scores.index(max_score) + 1 
        print ("/nPlayer", winner,"wins with a score of", max_score)

app = Application()
app.run()




