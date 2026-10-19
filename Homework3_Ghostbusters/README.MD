In Progress-

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
