Note: The resources, script, and test data for each problem can be found in the folders created for them 

Problem 1-----------

Introduction: 
Determine whether each line of an input text file is a palindrome and output True/False for each line and count each instance where is_palindrone(str) = True

Algorithm: 
The program reads each line, checks it with is_palindrome(), prints True or False for each line, and then prints the total number of palindromes.
is_palindrome() -
Removing any spaces from each line.
Compares to the reversed version which is initiated and tested with letters == letters[::-1]. This returns a boolean value
solve() -
This function strips the line ending from each line and loops for each line in the input file, looping the is_palindrome() function on each line of the input file. Because python counts True = 1 and False = 0, I was able to print the sum of the print boolean loop to get the count.
main() - 
This checks how the program was started and if the input was directed in the command prompt. This runs solve() on standard input if directed to, if not it will run on palindrome_input.txt if saved in the same folder. If the file entered via standard input was not found or if the palindrome_input.txt file was not found in the same folder, it will return an error message stating the file was not found. 

Interesting Facts:
- This program accepts input data in two ways. It accepts data via standard input if directed to, but if there isn't a specific .txt file entered, input data defaults to the palendrome_input.txt file if saved within that folder.
- Though it's stated that there will be no blank lines, blank lines are still skipped in case you paste anything into the input file and it leaves a blank last row. 
How to run (command prompt):
1) cd C:\Users\... <- this should point to where you saved the files
2a) python3 problem1_v3.py < palindrome_input.txt
2b) python3 problem1_v3.py 

Problem 2-----------

Introduction:
Find every unique substring of a string read from an input text file, using recursion. This program prints each unique substring in alphabetical order and counts the total number of unique substrings for the text input. 
Algorithm:
My unique_sustrings program searches using two levels of recursion and going through each pair, determines which are unique, sorts them, prints, and then counts the results. 
Recursion- 
1) collect_from(text, start, end, found) - this recursive function sets a starting point in the string and adds text[start:end] to found. It then calls itself on end + 1 to make the substring one character longer. It stops once end goes past the last position of the string.  
2) collect(text, start, found) - this recursive function calls collect_from() on each starting point by calling itself on start+1, finding all of the start and end points for a string. These two recursive functions working together will go through each start and end point where start < end
Remove dupes and Sort-
found is a set, and a set only keeps one copy of each value. Every substring is added to found, and when a substring that's already there is added again (like "ab" in "abcab"), the set ignores it. After the recursion finishes, sorted(found) puts the substrings in alphabetical order, and len() gives the total count.

Interesting Facts:
- Similarly to problem1, this program runs on standard input when directed, but if not directed to a specific file it will look for problem2_input.txt and run that if in the same folder.
- Having two levels of recursion here allows for cleaner running of the program, completing one starting position at a time and not continuing to the next starting position until the end string is reached from the previous starting point. I liked this method because it follows the same rules I was following subconsciously when writing this out (ex: input = car -> c, ca, car, a, ar...)

How to run (command prompt):
1) cd C:\Users\... <- this should point to where you saved the files
2a) python3 problem2.py < problem2_input.txt
2b) python3 problem2.py

Problem 3-----------

Introduction:
My program uses recursion to reverse a stack implemented as an array, singly linked list, and a doubly linked list. The program pushes the numbers 1-10 into a stack, prints the stack, reverses, and then prints the reversal. Each stack supports push, pop, peek, and is_empty

Algorithm:
Classes are created for each stack type, with the core of each being the recursive reverse_from function for each class. 
ArrayStack.reverse_from(low,high) - this swaps the low and high position, then calls itself on low+1 and high-1, moving inward until the low and high meet in the middle.

SinglyLinkedStack reverse_from(prev, node)- reverse() starts reverse_from() at the head with prev set to None. Each call points the current node's next back at the previous node, then calls itself on the following node. Since prev starts as None, the old head becomes the new tail with its next set to None. When reverse_from() runs past the last node, it returns the old bottom node, and reverse() sets it as the new head.

DoublyLinkedStack.reverse_from(node) - this recursive function swaps a nodes prev and next, then calls itself on the following node. Once each node has the prev and next swapped, reverse() swaps the head and tail.

Interesting Facts:
- HW2 was the first time I created a linkedlist, which helped lay out some of the foundational structures with this one. 
- No new stacks are created when the reveral happens for these. The reversal functions are acting on the existing stack rather than reading it backwards.

How to run (command prompt):
1) cd C:\Users\... <- this should point to where you saved the file
2) python3 problem3_v3.py

Problem 4-----------

Introduction: With n Ghostbuster and ghost pairs from an input text file, if they shot an infinitely long beam, would the busters be able to eliminate all ghosts in one shot without intersecting? Simply said, are the lines between all busters and their paired ghosts parallel? If the lines are all parallel, the program prints "All Ghosts: were eliminated" if their beams cross, it will print "All Ghosts: were not eliminated".

Algorithm: 
The core of this algorithm is built off using the fractions module to compute the rise over run from buster(n) to ghost(n), then checking to see if any of the slopes did not match. The catch with only using slopes to compare is that two streams with the same slope can be on the same line, which counts as crossing, so it also checks that no two streams share a y-intercept. 

slope(bx, by, gx, gy) - This finds the rise (gy - by) and the run (gx - bx) and returns rise/run. If the run is 0 the stream is vertical, so instead of dividing by 0 it returns "vertical". I used Fraction so the slope stays exact (ex: 1/3 stays 1/3 instead of 0.333...). 

intercept(bx, by, m) - This returns the y-intercept of the stream's line using b = y - mx. For a vertical stream there isn't a y-intercept, so it returns the x value instead, since every vertical line has its own x. 

all_eliminated(pairs) - This builds a list of every stream's slope. If the set of slopes has more than one value, the streams aren't parallel and it returns False. If all the slopes match, it builds a list of every stream's intercept. A set only keeps one copy of each value, so if the set of intercepts is shorter than the list, two streams are on the same line and it returns False. Otherwise it returns True. 

read_pairs() / solve() - read_pairs() reads n from the first line, then pulls the four numbers out of each "B <x> <y> G <x> <y>" line. solve() runs all_eliminated() on standard input and prints the result.

Interesting Facts:

Unlike problems 1 and 2, this program only runs on standard input, so the input file is always entered in the command. I left out the default file fallback to keep the program shorter.
My first idea was to only compare slopes, but that gets two of the examples wrong. B 0 0 G 2 2 and B 5 5 G 7 7 both have a slope of 1, but they're on the same line so the ghosts were not eliminated, which is why the intercept check is needed. B 1 0 G 1 6 has a run of 0, which would crash on divide by zero, which is why vertical streams are handled separately.
Using Fraction instead of normal division means there are no floating point rounding errors when comparing slopes and intercepts.
ghostbusters_input_10.txt is the same as ghostbusters_input_9.txt with the last pair repeated. Input 9 is eliminated, but input 10 is not, since the repeated pair has the same slope and the same intercept.
Besides the provided input files, I added the 4 examples from the assignment and 4 edge cases (a single Ghostbuster, vertical streams on the same line, parallel streams pointing in opposite directions, and a fraction slope). I also checked every input against a separate brute force version that compares every pair of streams, and they all matched.

How to run (command prompt):

cd C:\Users... <- this should point to where you saved the files
python3 ghostbusters.py < ghostbusters_input_1.txt <- any of the input files in the Problem4 folder can be used here
