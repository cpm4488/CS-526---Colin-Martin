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

Interesting Facts:

How to run:

