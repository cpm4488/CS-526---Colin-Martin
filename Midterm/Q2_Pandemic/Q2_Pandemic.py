import sys

#how far to move (rows, columns) to reach each neighbor, row 0 is the top
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

#neighbors of a county that are still on the board
def neighbors(row, col, n):
    for row_step, col_step in DIRECTIONS:
        next_row = row + row_step
        next_col = col + col_step
        if 0 <= next_row < n and 0 <= next_col < n:
            yield next_row, next_col

#spreads the infection using a running count of infected neighbors for each county
def spread(n, starting):
    infected = [[False] * n for _ in range(n)]
    sick_neighbors = [[0] * n for _ in range(n)]
    stack = []
    #mark every starting county before spreading so none get pushed twice
    for row, col in starting:
        if not infected[row][col]:
            infected[row][col] = True
            stack.append((row, col))
    total_infected = len(stack)
    while stack:
        row, col = stack.pop()
        #tell each neighbor it has one more infected neighbor
        for next_row, next_col in neighbors(row, col, n):
            sick_neighbors[next_row][next_col] += 1
            #a healthy county with 2 infected neighbors gets infected and spreads later
            if not infected[next_row][next_col] and sick_neighbors[next_row][next_col] == 2:
                infected[next_row][next_col] = True
                stack.append((next_row, next_col))
                total_infected += 1
    return total_infected

#reads n and the starting infected counties, then prints the result
def solve(source):
    lines = [line.split() for line in source if line.strip()]
    n = int(lines[0][0])
    starting = [(int(row), int(col)) for row, col in lines[1:]]
    if spread(n, starting) < n * n:
        print("There are healthy counties left")
    else:
        print("There are no healthy counties left")

if __name__ == "__main__":
    solve(sys.stdin)
