In Progress

Problem 1 (Snowfall) --------------------------------------------

--Introduction: 
The overall goal of this algorithm is to see if there are three consecutive days from a cumulative snowfall total which add up to > half the total amount recorded. The first row of the input file is n many days in the record, and the second row is the cumulative snowfall total by day for that period. 

The desired output for this algorithm is the input array + "solution: [YES/NO]". If there are three consecutive days which combined multiplied by 2 is greater than the total snowfall, the solution will display "YES" and if not it'll print "NO".

--Algorithm:
Core Idea- If there are three consecutive days which sum is > 1/2 total, one of those days would be the point that crosses 1/2 the total snowfall. With this being known, we will only need to find the total, midpoint, and days surrounding the midpoint to solve this.

Core Functions-
halfway_day(A, total, low, high):
This recursive function is a binary search where 2 * cumulative total > total snowfall. Rather than starting from the first day and walking through day by day, it starts at day n/2 and calls itself on the left/right half depending on if 2*cumulative total > or < total snowfall (similar to finding root with bisection). This function stops when the low and high meet.

three_over_half(A, n):
This uses a loop for the range of 2 above/below or the days around the halfway day, then finds the difference between the starting and endpoint of the three day cumulative snowfall totals, multiplies this by 2 and compares against the total. 
This will determine if those three days combined contributed to more than 1/2 of the total snowfall. This function also accounts for lists with <3 days and determines them as False because they do not contain 3 consecutive days.

General Flow- 
Input data entered via stdin gets identified by the solve() function, the halfway_day() function finds the day number which crosses the halfway point of the total snowfall. Then the three_over_half() function checks the three days grouping which include the crossover day to see if any of them *2 > total snowfall. This returns True or False accordingly, which then gets interpreted by the solve() function for the final output.  

--Interesting Facts:
- My first idea was to use where the halfway mark falls to only check the half of the array with fewer days. That would still check about n/2 windows, which grows with n. Checking only the windows that contain the halfway day is at most 3 windows no matter what n is. The binary search is the only part that grows with n, and it only takes about log2(n) steps (3 steps for 8 days).
- The halfway day works very similarly to root finding using the bisection methods, I'm learning about this in my other class which helped me think of the best way to search for the halfway point.
- I was originally going to divide the total by 2 for the comparison, but to avoid point division I changed it to multiply the three day sum by 2 and compare it to the total so everything remains an int.

--How to run (command prompt):
cd C:\Users... <- this should point to where you saved the files python3 Q1_Snowfall.py < snowfall_input1.txt 
when running for input files 2,3,4, & 5 change the file name accordingly

Problem 2 (Pandemic) --------------------------------------------

--Introduction: The goal of this algorithm was to simulate a virus spreading across a grid n x n in size with each space representing a healthy or infected county, then simulating the spread to see if it was able to infect all counties. The virus will spread to another county if two of its neighbors (Directly Up/Down/Left/Right) are infected. The first row of an input file is represents the size of the grid, and the following rows are the coordinates for the initial infected counties.

The desired output for this is "There are healthy counties left" or "There are no healthy counties left" based on the results from the simulation.

--Algorithm:
Core Idea- Every county counts the number of it's infected neighbors, once the count == 2, then it gets reclassified as infected and adds 1 to each uninfected neighbors' sick count when popped from the infected stack. Newly infected counties get added to a stack and then when popped they add 1 to their neighbors' sick count and this continuing until the stack is empty (no more possible infections). The code is initiated by defining the starting coordinates as infected, adding them to the stack then using a while loop to run the function until the stack is empty.

Core Functions- 
neighbors(row, col, n):
This uses the defined row and column steps (UP/DOWN/LEFT/RIGHT) to find a county’s neighbors, and skips any that would fall off the board, so counties on an edge or corner just end up with fewer neighbors. It’s called each time a county is popped off the stack to find which counties to add 1 to.

spread(n, starting):
This function is the heart of the algorithm, it simulates the spread of the disease. It starts with a grid that sets the infected status to False for all counties, then the input coordinates (starting infected) are fed into the grid, changing their infected status to True, and each one is pushed onto the stack. The while stack: loop then pops one infected county at a time and adds 1 to each of its neighbors’ sick_neighbors count. Once a healthy county’s sick neighbor count hits 2, it's then marked as infected and is pushed onto the stack so it can spread to its own neighbors. The loop stops when the stack is empty, meaning there are no more counties that can be infected.

General Flow:
Input data is processed in the solve() function, then the starting infected coordinates are fed into the spread() function which runs the simulation which for infected counties uses the neighbors() function to adds 1 to healthy neighboring counties. The determination is also stated in the solve definition and compares the number of the final total infected counties against n x n.

--Interesting Facts:
- This idea stood out as being a good idea because I'm pretty familiar with using stacks from some of the topics we've gone over in class and in the homework.
- The stack doesn't go from one day at a time, but doing a day by day movement is not necessary when using stacks and referencing the sick neighbors of a county because once a county is infected, it stays infected.
- Starting counties are marked infected before anything is popped so nothing will need to get pushed more than once.

--How to run (command prompt):

1) cd C:\Users\... <- this should point to where you saved the files
2) python3 Q2_Pandemic.py < pandemic_input1.txt or pandemic_input2.txt

Problem 3 (Symbol Puzzle Game) --------------------------------------------

--Introduction:
The goal of this algorithm is to take symbols and coordinates and see if their placements would be valid using sudoku rules (1 unique value per row, column, and subsquare). The input file contains the n x n board with n unique symbols and dots representing empty spaces. If the input it meets the sudoku rules, the output will print "The board is valid" and if not, it'll print "The board is invalid".

--Algorithm:
Core Idea- Track each row, column, and subsquare for each symbol. The valid symbols are read in the second row and each has list of sets (row, column, and subsquare) which get added to when looping through the rows and columns. If any the symbols row, column, or subsquare is already in it's set, the board is invalid. I decided to define the subsquare by dividing the x and y coordinate by the sqrt(n) and only taking the integer value of the quotients. 

Core Functions- 
is_valid(n, symbols, board):
This is the heart of this algorithm because it does all of the processing needed to determine whether or not the board is valid. This function uses the math library to find the sqrt(n), then defines seen() which contains the sets for rows, columns, and subsquares the symbol has been in. This then loops through each cell, skipping over empty cells. While moving through each cell, if any undefined symbols are found, the board is ruled invalid.
Rows and columns are processed directly into the sets and subsquares are processed with the calculating row // sqrt(n) and column // sqrt(n) which only returns the int value of the quotient. If the symbol has already been in one of the sets, it returns the board as invalid and if not it continues through the rest of the board.

General flow- 
Input data entered via stdin then read by the solve() function which "creates" the board and sets up the valid symbols by reading the second row. The solve function then runs by referencing the is_valid() function on the board. The is_valid() function then will return a determination which is processed to print if the board is or is not valid.

--Interesting Facts:
- This one was intriguing because I absolutely love sudoku; for fun often times i'll generate a valid boards from an empty grid. I honestly would just rely on visual queues to do this, so this let me take a second back to really think about what my brain is processing subconsciously and turn it into logic. This is where I got the idea to take the int value of x/y divided by root n, because when I do this and am focused on subsquares I see the 9x9 board as being 3x3. 

--How to run (command prompt):
1) cd C:\Users\... <- this should point to where you saved the files
2) python3 Q3_Sudoku.py < puzzle_game_input1.txt (For input files 2, 3, & 4, change the file name accordingly)

