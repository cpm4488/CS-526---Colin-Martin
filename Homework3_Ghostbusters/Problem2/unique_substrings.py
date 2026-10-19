import os
import sys

INPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "problem2_input.txt")

# substrings starting at start
def _collect_from(text, start, end, found):
    if end > len(text):
        return
    found.add(text[start:end])
    _collect_from(text, start, end + 1, found)

#substrings from each start
def _collect(text, start, found):
    if start >= len(text):
        return
    # All substrings from here
    _collect_from(text, start, start + 1, found)
    _collect(text, start + 1, found)

# only unique substrings, alphabetical order
def find_substrings(text):
    found = set()
    _collect(text, 0, found)
    return sorted(found)

# read, find, and print results
def solve(source):
    text = source.readline().rstrip("\r\n")
    sys.setrecursionlimit(max(1000, len(text) + 100))
    substrings = find_substrings(text)
    for substring in substrings:
        print(substring)
    # Total count
    print(len(substrings))

def main():
    if sys.stdin is not None and not sys.stdin.isatty():
        solve(sys.stdin)
        return
    if os.path.exists(INPUT_FILE):
        with open(INPUT_FILE) as source:
            solve(source)
    else:
        print(f"Could not find {INPUT_FILE}")

if __name__ == "__main__":
    main()
