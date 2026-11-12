In progress

Problem 1 (Binary Search Tree) --------------------------------------------

--Introduction:
The goal of this problem is to build a binary search tree from two ADTs, a Node and a BST. The program randomly generates an input set of 5 to 50 numbers between 1 and 1000, prints the input set and initial tree, then exercises add and delete while printing the tree after every method invocation. Last, it randomly generates numbers between 1 and 1000 to show both a positive (found) and negative (not found) case for find.

--Algorithm:
Core Idea- Everything to the left of a node is <= the node and everything to the right is bigger, so every operation is a series of left/right decisions starting from the root.

BST-
add_node(value): Makes the value the root if the tree is empty, otherwise calls add() on the root. Duplicates go left.
find_node(value): Calls find() on the root and returns True or False.
delete_node(value): Calls the recursive _delete() on the root. _delete() goes left or right until it finds the value, then returns what should take that node's place: its right child if it has no left child, its left child if it has no right child, or itself if it has two children, after copying in the largest value from the left subtree and deleting that value from the left subtree. Each parent sets its left or right child to whatever the call returned, so the tree reconnects itself on the way back up.
print_tree(): Calls inorder() on the root, which prints the values from smallest to largest.

General Flow-
main() builds the tree from the input set, adds 3 random values, deletes 3 values sampled from the input set so they're still in the tree, and then loops through random numbers with find_node() until both a positive and negative case are printed.

--Interesting Facts:
- I picked the largest value on the left for two children deletes because my tree sends duplicates left. Using the smallest value on the right could move a duplicate to the right of an equal value.
- Since in-order traversal of a BST always comes out sorted, a printed tree that isn't sorted would mean add or delete broke the tree.
- The find loop is needed because the tree only holds up to 50 of the 1000 possible numbers, so a positive case can take dozens of tries.
- The class layout is based on Joe James' "Python: Binary Search Tree - BST" video (https://youtu.be/YlgPi75hIBc), changed so duplicates go left and delete uses the largest value on the left.

--How to run (command prompt):
1) cd C:\Users\... <- this should point to where you saved the files
2) python3 Problem1_BST.py

Problem 2 (Morse Code Vowels) --------------------------------------------

--Introduction:
Count the number of ways a sequence of dots and dashes can be split into only vowels (E ., A .-, I .., O ---, U ..-), using every symbol. The input file has the number of symbols and the symbols on two rows. The output is the file name and the number of combinations.

--Algorithm:
Core Idea- 
This uses the table from class, with each symbol as a column and each vowel (E ., A .-, I .., O ---, U ..-) as a row. Going through the columns left to right, each cell counts the number of ways to spell everything up to that column if the last letter is that vowel. If the symbols ending at that column match the vowel's code, the cell copies the total from the column from just before vowel started, otherwise the cell is 0. Adding up a column gives the total number of ways to get to that column, and the total of the last column is the answer.

Core Functions-
count_vowel_combinations(symbols):
This is the heart of the algorithm. It keeps a list called total where total[column] is the number of ways to spell everything up to that column. total[0] starts at 1 because there is one way to spell nothing. For every column it checks all 5 vowels: start is the column just before where a vowel would begin at (column - the length of its code), and if the symbols from after start through the column column match the code, total[start] is added to total[column]. The function returns the total of the last column.
read_input(source): Reads the number of symbols, then the symbols.

General Flow-
solve() opens the file, reads it with read_input(), and prints the file name and the number of combinations from count_vowel_combinations().

--Interesting Facts:
- I only keep the total row of the table instead of every cell. Each cell is just a copy of an earlier total, so it can be added straight into the column's total.
- The longest vowel code is 3 symbols, so each column only ever looks back 1, 2, or 3 columns.
- vowel_input3.txt is 0 because of the two dashes at columns 13 and 14 (.--.). A dash can only be the end of an A or U (which need a dot right before the dash) or part of an O (which needs three dashes in a row), so nothing fits there. Every column after that copies a 0, so the answer stays 0 even though the first 13 symbols can be read 6 different ways.

--How to run (command prompt):
1) cd C:\Users\... <- this should point to where you saved the files
2) python3 Problem2_Vowels.py vowel_input1.txt (For input files 2, 3, and 4, change the file name accordingly)
   Paste below this to run all example problems at once:
	python3 Problem2_Vowels.py vowel_input1.txt vowel_input2.txt vowel_input3.txt vowel_input4.txt

Problem 3 (Longest Alternating Sequence) --------------------------------------------

--Introduction:
The goal of this algorithm is to take two sequences of integers, A and B, and find the longest sequence X that alternates between them. The values in X have to increase, every other value has to come from the other sequence, and each value has to come from a later position than the value before it (two values can't come from the same position). The first row of the input file is the size of A, the second row is the size of B, the third row is A, and the fourth row is B.
 
The input file name is typed after the script name, and the desired output is the file name and the length of the longest sequence:
File Input: longest_seq1.txt
Longest Sequence: 4
 
--Algorithm:
Core Idea- Every value asks one question: "what is the longest sequence I can end?" To answer it, a value from A looks for the best sequence that ended in B, in an earlier position, with a smaller value, and adds 1 to its length (B does the same thing looking at A). Going through the positions from left to right means every earlier answer is already finished when it's needed. The slow part is finding "the best sequence below this value", so I keep one segment tree for A and one for B, ordered by value, which can answer that in O(log n) instead of checking every earlier value.
 
Core Functions-
SegmentTree:
This is based on the GeeksforGeeks efficient segment tree. The tree is stored in one list where the leaves (one per value) are at tree[n] to tree[2n - 1] and node i's children are 2i and 2i + 1. Each spot holds an entry (length, row, position) for the best sequence ending at that value, and each node above holds the best entry from its whole block of values.
- update_tree_node(p, value): Keeps the larger entry at spot p, then walks up to the root recomputing each parent as the max of its two children.
- query(l, r): Returns the best entry from spot l up to but not including spot r. It starts at the two leaves and moves up a level at a time, taking a node by itself when its parent would reach outside the range.
 
best_ending_here(value, row, position, other_tree, spot, previous):
This is the heart of the algorithm. It queries the other row's tree for the best entry below this value, saves which value it came from in previous, and returns that length + 1. If nothing smaller has been seen, the query returns an empty entry with length 0, so the value starts a new sequence of length 1.
 
longest_alternating(A, B):
This gives each different value a spot in the trees (smallest value gets spot 0), then loops through every position. At each position it looks up the A value and the B value first, then adds both to their trees. Doing both lookups before either add is what keeps two values from the same position from being used together. It keeps track of the best entry seen overall.
 
build_sequence(A, B, previous, best):
This starts at the end of the best sequence and follows the previous links backwards until it reaches the start, then reverses the list.
 
General Flow-
solve() reads the input with read_input(), runs longest_alternating() to get the longest sequence, and prints the file name and the length of the sequence.
 
--Interesting Facts:
- The simple way to solve this compares every value to every earlier value in the other sequence, which is O(n^2). The segment tree version is O(n log n) and runs extremely efficiently. I used claude to generate a larger test file (longest_seq7.txt, 25,000 values in A and 30,000 in B) to check how it scales, it ran in about half a second (insane!), with a longest sequence of 301.
- The segment tree is changed from the GeeksforGeeks version (https://www.geeksforgeeks.org/dsa/segment-tree-efficient-implementation/) in a few ways:
 a) It keeps the max instead of the sum 
 b) Update keeps the larger entry instead of overwriting (two values in the same sequence can be equal)
 c) I made it a class so A and B can each have their own tree, and there's no build step because the trees start empty and fill up as the positions are read.
- The query in the article leaves out the right end of the range, which works out perfectly here since query(0, spot) is exactly "every value smaller than this one".
- Some inputs (longest_seq3.txt and longest_seq4.txt) have more than one sequence of the longest length. The sequence found depends on how ties are broken, but the length is always the same.
 
--How to run (command prompt):
1) cd C:\Users\... <- this should point to where you saved the files
2) python3 Problem3_LongestAlternating.py longest_seq1.txt (For input files 2, 3, 4, 5, and 6, change the file name accordingly)
   Paste below this to run all example problems at once: 
	python3 Problem3_LongestAlternating.py longest_seq1.txt longest_seq2.txt longest_seq3.txt longest_seq4.txt longest_seq5.txt longest_seq6.txt
