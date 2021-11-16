"""
In this hopping game, there are 'n' squares and the player can either jump 1 square or 2 squares at a time. 
This program uses recursion to generate all the possible hopping paths the player can take.

Author: Jean-Philippe Le Blanc
Section #: 002
Student #: 20157203
Date: November 15, 2021
"""


# hopping_game is a recursive function that returns a list of all possible hopping paths a player can take
def hopping_game(n, path=""):
    if n == 0: # Base case: the player has made it to the last tile, add string '0' 
        return ["0" + path] # Return the entry of the list
    elif n == 1: # Base case: the player has made it to the second last tile, add string '0-1' as that is the only possible move at this square. 
        return ["0-1" + path] # Return the entry of the list
    else: 
        # Recursively call hopping_game with the updated 'n' value and updated 'path' string
        return hopping_game(n-1, f"-{n}{path}") + hopping_game(n-2, f"-{n}{path}") 
        
# main function takes care of testing hopping_game function      
def main():
    print(hopping_game(3))
    print(hopping_game(4))
    print(hopping_game(5))
    return 0

# main() call to start the program
main()