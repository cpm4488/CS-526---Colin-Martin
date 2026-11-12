import sys

#segmenttree based on the GeeksforGeeks efficient segment tree, changed from sum to max

#entries are (length, row, position), an empty spot has length 0
EMPTY = (0, "", -1)

#leaves are tree[n] to tree[2n - 1], and node i's children are 2i and 2i + 1
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [EMPTY] * (2 * n)

    #keeps the larger entry at spot p, then updates each parent above it
    def update_tree_node(self, p, value):
        p = p + self.n
        self.tree[p] = max(self.tree[p], value)
        i = p // 2
        while i >= 1:
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            i = i // 2

    #best entry from spot l up to but not including spot r
    def query(self, l, r):
        res = EMPTY
        l = l + self.n
        r = r + self.n
        while l < r:
            if l % 2 == 1:
                res = max(res, self.tree[l])
                l = l + 1
            if r % 2 == 1:
                r = r - 1
                res = max(res, self.tree[r])
            l = l // 2
            r = r // 2
        return res

#longest sequence ending at this value, built on the best one in the other row below it
def best_ending_here(value, row, position, other_tree, spot, previous):
    length, previous_row, previous_position = other_tree.query(0, spot[value])
    previous[(row, position)] = (previous_row, previous_position)
    return (length + 1, row, position)

#follows the previous links back from the end of the best sequence
def build_sequence(A, B, previous, best):
    length, row, position = best
    sequence = []
    while position != -1:
        if row == "A":
            sequence.append((A[position], row, position))
        else:
            sequence.append((B[position], row, position))
        row, position = previous[(row, position)]
    sequence.reverse()
    return sequence

#finds the longest increasing sequence that switches rows and moves forward in position
def longest_alternating(A, B):
    #each different value gets a spot in the trees, smallest value gets spot 0
    values = sorted(set(A + B))
    spot = {value: index for index, value in enumerate(values)}
    tree_A = SegmentTree(len(values))
    tree_B = SegmentTree(len(values))
    previous = {}
    best = EMPTY

    for position in range(max(len(A), len(B))):
        has_A = position < len(A)
        has_B = position < len(B)

        #look up both rows before adding either, so two picks can't share a column
        if has_A:
            entry_A = best_ending_here(A[position], "A", position, tree_B, spot, previous)
        if has_B:
            entry_B = best_ending_here(B[position], "B", position, tree_A, spot, previous)

        if has_A:
            tree_A.update_tree_node(spot[A[position]], entry_A)
            best = max(best, entry_A)
        if has_B:
            tree_B.update_tree_node(spot[B[position]], entry_B)
            best = max(best, entry_B)

    return build_sequence(A, B, previous, best)

#read the length of A, the length of B, then A and B
def read_input(source):
    lines = [line.split() for line in source if line.strip()]
    n = int(lines[0][0])
    m = int(lines[1][0])
    A = [int(value) for value in lines[2][:n]]
    B = [int(value) for value in lines[3][:m]]
    return A, B

#read the file, solve, and print the file name and the length of the longest sequence
def solve(file_name):
    with open(file_name) as source:
        A, B = read_input(source)
    sequence = longest_alternating(A, B)
    print("File Input:", file_name)
    print("Longest Sequence:", len(sequence))
    print()

#runs every file name typed after the script name
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Type the input file after the script name, ex: python3 longest_sequence.py longest_seq1.txt")
    for file_name in sys.argv[1:]:
        solve(file_name)
