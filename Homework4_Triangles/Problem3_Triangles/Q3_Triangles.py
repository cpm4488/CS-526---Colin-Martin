import sys
from math import gcd 

#finds greatest common divisor of two numbers using euclid's algorithm
#hased this one out because the function from math was faster 
#def gcd(a, b):
#    a, b = abs(a), abs(b)
#    while b:
#        a, b = b, a % b
#    return a

#uses gcd to minimize the vector from coords p -> q
def direction(p, q):
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    g = gcd(dx, dy)
    return dx // g, dy // g

#rotate 90 degrees counter clockwise
def perpendicular(d):
    dx, dy = d
    return -dy, dx

#right angles with their corner at p
def count_corner(p, points):
    #count of points in each direction from p
    directions = {}
    for q in points:
        if q != p:
            d = direction(p, q)
            directions[d] = directions.get(d, 0) + 1
    count = 0
    #only look 90 degrees one way so each pair of directions is counted once
    for d, how_many in directions.items():
        count += how_many * directions.get(perpendicular(d), 0)
    return count

#one right angle per triangle, so only count the corners with right angles
def count_right_triangles(points):
    return sum(count_corner(p, points) for p in points)

#read n then one point per line
def read_points(source):
    lines = [line.split() for line in source if line.strip()]
    n = int(lines[0][0])
    return [(int(x), int(y)) for x, y in lines[1:n + 1]]

#read, count, and print result
def solve(source):
    points = read_points(source)
    print("The number of right triangles is:", count_right_triangles(points))

if __name__ == "__main__":
    solve(sys.stdin)
