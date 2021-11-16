# a4
Deliverables:

Submit two .py files named A4_1.py and A4_2.py. Do NOT zip the files, otherwise you lose two points. Make sure and double check that your files are submitted successfully!

Your programs should follow Python 3 style guide (http://sites.cs.queensu.ca/courses/cisc121/cisc_121_python_3_style_guide.html) and include proper inline comments, following a “#” sign, and docstrings, enclosed by a pair of triple double-quotes, as the prologue of each of your programs. Your programs should also meet the requirements exactly as described as follows. 

Your assignment will be graded by a rubric, out of 20 points, 10 points for each question, on functionality (correctness), programming style (clear logic and flow), documentation (docstrings and comments).

 

A4_1 Binary search

Write a recursive binary search function, find_first_b, in A4_1.py that returns the index of the first “b”, given a string containing only “a”s and “b”s. All the “a”s are to the left of all the “b”s. 

For example,

string “aabbb” returns 2;

string “aaaaaaaa” returns None;

string “bbb” returns 0;

string “aaaaaab” returns 6.

Provide three testing cases in the module testing code.

  

A4_2 Hopping game

Anna is playing a hopping game, where there are n squares lined up on the ground. Anna can either hop one square or two squares at a time. Write a recursive function hopping_game(n) in A4_2.py that takes the number of squares, n, as input and returns a list of all possible hopping paths. 

For example,

hopping_game(1) returns [“0-1”]  # meaning one path jumping from start 0 to square 1

hopping_game(2) returns ['0-1-2', '0-2']  # meaning two paths, jumping from start 0 to square 1 and then to square 2, # or jumping from start 0 to square 2

hopping_game(3) returns ['0-1-2-3', '0-2-3', '0-1-3']

hopping_game(4) returns ['0-1-2-3-4', '0-2-3-4', '0-1-3-4', '0-1-2-4', '0-2-4']

And so on. 

Provide three testing cases in the module testing code.

 
