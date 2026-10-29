import sys
import math

EMPTY = "."

#x and y divided by sqrt(n) allows you to check for rows,columns, and subsquares(int value of quotient)  
def is_valid(n, symbols, board):
    #square root of n is the size of each sub-square (3 for a 9x9 board)
    box_size = math.sqrt(n)
    #for each symbol, the rows, columns, and sub-squares it has already been in
    seen = {symbol: (set(), set(), set()) for symbol in symbols}
    for row in range(n):
        for col in range(n):
            symbol = board[row][col]
            #empty cells never make the board invalid
            if symbol == EMPTY:
                continue
            #symbols not in the list are invalid
            if symbol not in seen:
                return False
            rows, cols, boxes = seen[symbol]
            #integer parts of row / root n and col / root n name the sub-square
            box = (row // box_size, col // box_size)
            #this symbol was already in this row, column, or sub-square
            if row in rows or col in cols or box in boxes:
                return False
            rows.add(row)
            cols.add(col)
            boxes.add(box)
    return True

#reads n, the symbols, and the board, then prints the result
def solve(source):
    #strip each line and skip blank lines
    lines = [line.strip() for line in source if line.strip()]
    n = int(lines[0])
    symbols = lines[1].split(",")
    board = [line.split(",") for line in lines[2:n + 2]]
    if is_valid(n, symbols, board):
        print("The board is valid")
    else:
        print("The board is invalid")

if __name__ == "__main__":
    solve(sys.stdin)