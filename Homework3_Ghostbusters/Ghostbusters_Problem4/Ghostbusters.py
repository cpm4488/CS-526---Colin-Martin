import sys
from fractions import Fraction

# rise over run from buster to ghost
def slope(bx, by, gx, gy):
    rise = gy - by
    run = gx - bx
    # vertical stream, can't divide by 0
    if run == 0:
        return "vertical"
    return Fraction(rise, run)

# where the stream's line is, y-intercept (or x for vertical streams)
def intercept(bx, by, m):
    if m == "vertical":
        return bx
    return by - m * bx

# same slope for every stream, and no two streams on the same line
def all_eliminated(pairs):
    slopes = [slope(bx, by, gx, gy) for bx, by, gx, gy in pairs]
    # different slopes, so the streams cross
    if len(set(slopes)) != 1:
        return False
    intercepts = [intercept(bx, by, slopes[0]) for bx, by, gx, gy in pairs]
    # repeated intercept, two streams on the same line
    return len(set(intercepts)) == len(intercepts)

# read B <x> <y> G <x> <y> lines
def read_pairs(source):
    lines = [line.split() for line in source if line.strip()]
    n = int(lines[0][0])
    pairs = []
    for parts in lines[1:n + 1]:
        pairs.append((int(parts[1]), int(parts[2]), int(parts[4]), int(parts[5])))
    return pairs

# read, check, and print result
def solve(source):
    pairs = read_pairs(source)
    if all_eliminated(pairs):
        print("All Ghosts: were eliminated")
    else:
        print("All Ghosts: were not eliminated")

if __name__ == "__main__":
    solve(sys.stdin)
