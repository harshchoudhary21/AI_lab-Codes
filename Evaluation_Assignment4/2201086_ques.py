import math
import random

def alphaBeta_Pruning(depth,sticks, is_maximum, a, b):
    if sticks == 1:
        return 1 if is_maximum else -1
    if depth  == 0:
        return 0
    if is_maximum:
        maxValue = -math.inf
        for i in range (1, min(4,sticks+1)):
            currValue = alphaBeta_Pruning(depth-1,sticks-i, False, a, b)
            maxValue = max(maxValue, currValue)
            a = max(a, currValue)
            if b <= a:
                 break
        return maxValue
    else:
        minValue = math.inf
        for i in range (1, min(4,sticks+1)):
            currValue = alphaBeta_Pruning(depth-1,sticks-i, True, a, b)
            minValue = min(minValue, currValue)
            b = min(b, currValue)
            if a <= b:
                break
        return minValue
def gameOfSticks():
    sticks = int(input("Enter the number of sticks: "))
    depth = int(input("Enter the depth of the game tree: "))
    player = random.choice([1, 2])
    
    print("Player", player, "starts the game first")
    
    while sticks > 0:
        print("Number of sticks left:", sticks)
        
        if player == 1:
            moves = int(input("Enter the number of sticks you want to take (1-3): "))
            while moves < 1 or moves > 3 or moves > sticks:
                print("You have entered an invalid number of sticks. Please try again.")
                moves = int(input("Enter the number of sticks you want to take (1-3): "))
        else:
            best_choice = 1
            best_score = -math.inf
            for i in range(1, min(3, sticks+1)):
                score = alphaBeta_Pruning(depth, sticks-i, False, -math.inf, math.inf)
                if score > best_score:
                    best_score = score
                    best_choice = i
            moves = best_choice
        
        print(f"Player {player} picks {moves} sticks.")
        sticks -= moves
        if sticks == 0:
            break
        player = 3 - player
    
    print(f"Player {3-player} wins!")

gameOfSticks()

              
        






            


   




