import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    
    return roll

while True:
   players = input("Enter the number of players(1-4): ")
   if players.isdigit():
       players = int(players)
       if 1 <= players <= 4:
           break
       else:
           print("Must be between 2-4 players.")
   else:
        print("Invalid, try again.")
        
max_scores = 50
players_scores = [0 for _ in range(players)]
        
while max(players_scores) < max_scores:
    
    for player_idx in range(players):
       print("\n Player number ", player_idx + 1, "turn has just started! \n")
       print("Your total score is: ", players_scores[player_idx], "\n")
       current_score = 0
    
       while True:
         should_roll = input("Would you like to roll(y): ")
         if should_roll.lower() != "y":
           break
           
         value = roll() 
         if value == 1:
           print("You rolled a 1! Turn done!")
         else:
           current_score += value
           print("You rolled a:", value)
           print("Your current score is " , current_score)   

       players_scores[player_idx] += current_score
       print("Your total score is: " , players_scores[player_idx])
       
max_scores =  max(players_scores)
winning_idx = players_scores.index(max_scores)
print("Players number", winning_idx + 1,"is the winner with the score of: ", max_scores)