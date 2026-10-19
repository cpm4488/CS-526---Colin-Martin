import os
import sys

INPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "palindrome_input.txt")

def is_palindrome(text):
    letters = text.replace(" ", "")
    return letters == letters[::-1]

def solve(lines):
    results = [is_palindrome(line.rstrip("\r\n")) for line in lines if line.strip()]
    for result in results:
        print(result)
    print(sum(results))

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
