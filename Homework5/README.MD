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
