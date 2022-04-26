#%%
# Game Rock Paper Scissors
from numpy import random
choices = ['rock', 'paper', 'scissors']

#p1 = random.choice(choices)
#p2 = random.choice(choices)

class RPS():
    
    def __init__(self, p1, p2):
        #input the players' names
        self.p1 = p1
        self.p2 = p2
        
    def game_play(self):
        #generate the players' choices
        p1_choice = random.choice(choices)
        p2_choice = random.choice(choices)
        
        #determines the winner
        #1. same output -> tie
        if p1_choice == p2_choice:
            self.result = "draw"
        
        #2. if different, from the perspective of p1
        else:
            if p1_choice == "rock":
                if p2_choice == "paper":
                    self.result = "p1 loses, p2 wins"
                elif p2_choice == "scissors":
                    self.result ="p1 wins, p2 loses"
            elif p1_choice == "paper":
                if p2_choice == "scissors":
                    self.result = "p1 loses, p2 wins"
                elif p2_choice == "rock":
                    self.result ="p1 wins, p2 loses"
            elif p1_choice == "scissors":
                if p2_choice == "rock":
                    self.result = "p1 loses, p2 wins"
                elif p2_choice == "paper":
                    self.result ="p1 wins, p2 loses"
        print(f"{self.p1} chooses {p1_choice}, {self.p2} chooses {p2_choice}, {self.result}")

ab = RPS("a","b")
ab.game_play()
#%%

