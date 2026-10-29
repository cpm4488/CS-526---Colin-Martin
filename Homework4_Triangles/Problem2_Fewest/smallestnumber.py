import sys

#take larger values first, the count that passes the target first is the smallest
def smallest_count(array, target):
    total = 0
    for count, value in enumerate(sorted(array, reverse=True), 1):
        total += value
        if total > target:
            return count

#read n, the target, then the array
def read_input(source):
    lines = [line.split() for line in source if line.strip()]
    n = int(lines[0][0])
    target = int(lines[1][0])
    array = [int(value) for value in lines[2][:n]]
    return array, target

#read, solve, and print the original array, target, and answer
def solve(source):
    array, target = read_input(source)
    answer = smallest_count(array, target)
    print("Input:", ",".join(str(value) for value in array), "Target:", target, "Answer:", answer)

if __name__ == "__main__":
    solve(sys.stdin)
