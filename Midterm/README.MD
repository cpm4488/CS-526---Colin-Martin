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

Problem 1 (Snowfall) --------------------------------------------
