"""
This program finds the first character 'b' in a string using a binary search algorithm and returns its index.
*Note: All the "a"s are to the left of all the "b"s

Author: Jean-Philippe Le Blanc
Section #: 002
Student #: 20157203
Date: November 15, 2021
"""


# find_first_b is a recursive binary search function that will find the index of the first 'b'
def find_first_b(a, lower, upper, index=None):
    if lower > upper: # Base case: the algorithm has searched the entire list, return pos
        return index

    mid = (lower+upper)//2 # Determine the mid index 
    if a[mid] == 'b': # Check if there is a 'b' at index m
        index = mid # Set pos to m to keep track of the index of the 'b'
        return find_first_b(a, lower, mid-1, index) # Check to see if there is another b in the first half of the list
    else: 
        return find_first_b(a, mid+1, upper, index) # Check if there is a 'b' in the second half of the list


# main function takes care of testing find_first_b function
def main():
    print(find_first_b("aaaaaaaaaaaaaaaaaaaaaaaaab", 0, len("aaaaaaaaaaaaaaaaaaaaaaaaab")-1)) # Index 25
    print(find_first_b("aaabbbbbbbbbbb", 0, len("abbbbbbbbbbb")-1)) # Index 3
    print(find_first_b("bbbbbbbbbbbbbbbbbbbbb", 0, len("bbbbbbbbbbbbbbbbbbbbb")-1)) # Index 0
    print(find_first_b("b", 0, len("b")-1)) # Index 0
    return 0


# main() call to start the program
main()