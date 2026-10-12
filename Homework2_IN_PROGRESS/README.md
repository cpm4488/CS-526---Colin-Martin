Hello Professor, 
I'm still working on this assignment. I'll update this once complete and will also give you a heads up via blackboard or email when ready. 
Thank you for understanding.
Colin

Problem1 - Answered in standalone txt file in the HW2 GitHub folder.

Problem2- 

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

Input Format (v = value idx = index location):
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

