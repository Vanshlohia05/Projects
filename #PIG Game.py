import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:  # Correct condition
            break
        else:
            print("Must be between 2-4 players.")  # Only print when the condition is not met
    else:
        print("Invalid input. Try again.")

print(players)

max_score = 50
players_scores = [0 for _ in range(players)]

print(players_scores)

while max(players_scores) < max_score:
    
    for plaer_idx in range(players):
        print("\nPlayer", plaer_idx +1, "turn has just started!")
        print("Your ttal score is:", players_scores[plaer_idx], "\n")
        current_score = 0
        
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score +=1
                print("You rolledd a:", value)
            
            print("Your score is:", current_score)

        players_scores[plaer_idx] += current_score
        print("Your total score is: ", players_scores[plaer_idx])
        

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score )