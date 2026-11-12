import sys

#create a table containing each vowel and its morse code
VOWELS = {"E": ".", "A": ".-", "I": "..", "O": "---", "U": "..-"}

#fills in the table one column at a time and returns the last total
def count_vowel_combinations(symbols):
    #total[column] is the number of ways to spell everything up to that column
    total = [0] * (len(symbols) + 1)
    total[0] = 1

    for column in range(1, len(symbols) + 1):
        for vowel in VOWELS:
            code = VOWELS[vowel]
            start = column - len(code)
            #only count if the symbols ending at this column match the vowel
            if start >= 0 and symbols[start:column] == code:
                total[column] = total[column] + total[start]
                
    return total[len(symbols)]

#read the number of symbols, then the dots and dashes
def read_input(source):
    lines = [line.split() for line in source if line.strip()]
    n = int(lines[0][0])
    symbols = lines[1][0][:n]
    return symbols

#read, solve, and print
def solve(file_name):
    with open(file_name) as source:
        symbols = read_input(source)
    print("File Input:", file_name)
    print("The Number of Vowel combinations is: ", count_vowel_combinations(symbols))
    print()

#runs every file name entered after the script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Type the input file after the script name, ex: python3 Problem2_Vowels.py vowel_input1.txt")
    for file_name in sys.argv[1:]:
        solve(file_name)
