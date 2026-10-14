***Recordings of executions located in problem2 and problem4 folders


Problem1-------------------------------- 
Answered in standalone txt file in the HW2 GitHub folder.

Problem2-------------------------------- 

For problem 2 I was tasked to create a singly linked list which can be read using a driver program to execute the following actions using standard in: 
- append 
- prepend 
- insert
- get
- find
- len
- update
- delete
- delete_at
- print_list

How it works: 
The key to my solution is knowing the expected input for my driver program based on the directive entered. The concept is that each input will be "directive", "directive" "value", "directive" "index", or "directive" "index" "value". A directive is always needed, so by establishing the expected order and number of input values we'll be able to run the program.

The singly linked list gives the directives from the driver something to point to in the other program. In the singly linked list class on the other python file, I defined all of the necessary tasks, rules, and index errors for the driver to point to. The core of the SinglyLinkedList class are node_loc() and and unlink(). The node_loc function is used to know positions and bounds of the list when walking, the unlink() function is used for removals and ensures the head, tail, and size remain correct.

How to run:
1. Save both the driver and singlylinkedlist files to the same folder
2. Execute the driver
3. Using standard in and the input format below, enter the actions into the terminal.

Input Format (v = value i = index location):
append v
prepend v
insert i v
get i
find v
len 
update i v
delete v
delete_at i
print_list


Problem 3-------------------------------- 
a) The bases of this function are n < 0, n == 0. The base n < 0 is used because it stops the recursion when overshooting zero and counts zero so that the unsuccessful path does not get counted. The base n == 0 is used to count a successful path because when n == 0, it proves that path added up to the total. Given this, ways(0) should be = 1 because that is used to identify one sucessful path and without ways(0) = 1 successful pathways could not be identified.
b) If we could only take two steps, we'd be using a structure very similar to what is used to create the Fibonacci sequence. This would be because each value would be the sum of the two before it and would be read as ways(n-1) + ways(n-2). 

Problem 4-------------------------------- 

For problem 4, my task was to create a doubly linked list that always keeps it's values in ascending order and also create a driver which can run the following actions using standard in:

- add
- delete
- exists
- count
- sum_middle_three
- median
- print_list

How it works:
Each node stores a value, a prev pointer, and the next pointer.The list keeps track of the head, tail, and size. The add function walks from the head until it finds the first value bigger than the new one, and inserts the new node right before it, so the list always stays sorted. Because each node has a prev pointer, the unlink() function can remove a node without walking to the node before it, which makes deleting more efficient than in how it was in problem2.

The exists, count, total, and print_line use recursive functions that act on one node and then call themselves on node.next. Because the list sorts on default, sorted, exists, count, and delete can stop once they reach the value they're looking for. Median will walk to the middle node, and either take that number, or if the list is even take the middle point of the middle two numbers.

How to run:

1) Save both the driver and SortedDoublyLinkedList files to the same folder
2) Execute the driver
3) Using standard in and the input format below, enter the actions into the terminal.

Input Format (v = value):
add v
delete v
exists v
count v
total
sum_middle_three
median
print_list
