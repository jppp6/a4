"""
This program

Author: Jean-Philippe Le Blanc
Section #: 002
Student #: 20157203
Date: November 15, 2021
"""

def hopping_game(n, s=""):
    if n == 0:
        return ["0"+s]
    elif n == 1:
        return ["0-1"+s]
    else:
        return hopping_game(n-1, f"-{n}"+s) + hopping_game(n-2, f"-{n}"+s)
        
        
        

        


def main():
    print(hopping_game(5))
    
    return 0

# main() call to start the program
main()