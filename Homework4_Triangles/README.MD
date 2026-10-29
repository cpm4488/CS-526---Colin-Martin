Problem 1 (Traversal Questions) --------------------------------------------
Answers found in Problem1 folder


Problem 2 (Smallest Number) --------------------------------------------

--Introduction: Find the smallest number of elements from an array whose sum is greater than a target T. The input file has n on the first row, T on the second, and the array on the third. The output is the original array, the target, and the answer (ex: "Input: 8,3,9,2,7,1,5 Target: 18 Answer: 3").

--Algorithm: 

Core Idea- The k biggest values make the largest sum any k elements can, so adding values from largest to smallest and stopping once the sum passes T gives the smallest count.

smallest_count(array, target): Sorts a copy of the array largest to smallest, adds values to a running total, and returns the count once the total is greater than the target. This is O(n log n) because of the sort.

General Flow- solve() reads the input with read_input(), runs smallest_count(), and prints the original array, target, and answer.

--Interesting Facts:

I used > instead of >= when comparing total to target because equaling the target doesn't count. In fewest_1.txt, 9 + 8 = 17 equals the target, so a third value is needed.

--How to run (command prompt):

cd C:\Users... <- this should point to where you saved the files
python3 smallestNumber.py < fewest_1.txt (For input files 2 & 3, change the file name accordingly)


Problem 3 (Right Triangles) --------------------------------------------

--Introduction:
The goal of this algorithm is to take n unique points on a grid then find how many unique right triangles can be made by choosing sets of three points. The first row of the input file is n, the number of points, and each row after that is one point's x and y coordinate. The program has to run in under 30 seconds.

The desired output for this is "The number of right triangles is:..."

--Algorithm:
Core Idea- A triangle can only have one right angle, so if I count the right angles at every point, each triangle only gets counted once. This turns the problem into: for each point p, how many pairs of other points make a 90 degree angle at p? To answer that, I treat p as the origin, find the direction from p to every other point, and count how many points are in each direction. Two directions are perpendicular if one is the other rotated 90 degrees, so the number of right angles at p is the count in one direction multiplied by the count in its perpendicular direction.

Core Functions-
gcd(a, b):
This function uses Euclid's algorithm to find the greatest common divisor of two numbers. It keeps replacing the pair with (b, a % b) until b is 0. abs() is used at the start so the gcd will always be positive.

direction(p, q):
This finds the vector from p to q (dx, dy) and divides both by their gcd so it's in its smallest form. This way points on the same ray from p have the same direction even if they're different distances away (ex: (0, 4) and (0, 7) both become (0, 1)). Using // keeps everything as an int.

perpendicular(d):
This rotates a direction 90 degrees counter clockwise, (dx, dy) becomes (-dy, dx).

count_corner(p, points):
This is the heart of the algorithm. It loops through every other point, finds its direction from p, and keeps a count for each direction in a dictionary. Then for each direction it looks up the count of its perpendicular direction and adds count * perpendicular count to the total. It only looks 90 degrees one way (counter clockwise) so each pair of directions only gets counted once.

General Flow-
Input data entered via stdin is read by the solve() function using read_points(), which reads n from the first line and turns each following line into an (x, y) point. count_right_triangles() then runs count_corner() with every point as the corner, which uses direction() and perpendicular() to count the right angles at that point, and adds them all up. solve() prints the total as the number of right triangles.

--Interesting Facts:
- Using the greatest common divisor here because it allowed me to find each point containing whole number coordinates on the vector which makes the matches exact when moving outward from the origin point.
- Rather than using math.gcf() to pull the greatest common divisor, I wanted to create the function myself because it seemed like a pretty simple function and I was curious to see if it was faster when scaling up the input to a much larger grid. Turns out it was actually slower because the match function runs in C++, I still decided to leave the manually written one in the script just because I like seeing how the function works. For testing these I used claude to generate a 5,000 point file to test this with as I didn't find the difference noticeable for the 1,000pt input (my script ran in ~14s while the math.gcf() ran in ~9s. 


--How to run (command prompt):
1) cd C:\Users\... <- this should point to where you saved the files
2) python3 rightTriangles.py < rightangles_1.txt (For input files 2 & 3, change the file name accordingly)
