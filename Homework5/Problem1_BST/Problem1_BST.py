import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #duplicates and smaller values go left
    def add(self, value):
        if value <= self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)

    def find(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left:
                return self.left.find(value)
            return False
        else:
            if self.right:
                return self.right.find(value)
            return False
    #Sets up an in order traversal to print
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value, end=" ")
        if self.right:
            self.right.inorder()

class Binarysearchtree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if self.root:
            self.root.add(value)
        else:
            self.root = Node(value)

    def find_node(self, value):
        if self.root:
            return self.root.find(value)
        return False

    def delete(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            pred = node.left
            while pred.right:
                pred = pred.right
            node.value = pred.value
            node.left = self.delete(node.left, pred.value)
        return node

    def delete_node(self, value):
        self.root = self.delete(self.root, value)

    def print_tree(self):
        if self.root:
            self.root.inorder()
            print()
        else:
            print("(empty)")

def main():
    size = random.randint(5, 50)
    input_set = [random.randint(1, 1000) for _ in range(size)]
    print("Input set (",str(size)," values):",sep="")
    print(" ".join(str(value) for value in input_set))

    tree = Binarysearchtree()
    for value in input_set:
        tree.add_node(value)
    print("\nInitial tree:")
    tree.print_tree()

    for _ in range(3):
        value = random.randint(1, 1000)
        print("\nadd_node(",str(value), ")",sep="")
        tree.add_node(value)
        tree.print_tree()

    #sampled from the input set so each value is still in the tree when it is deleted
    for value in random.sample(input_set, 3):
        print("\ndelete_node(",str(value),")",sep="")
        tree.delete_node(value)
        tree.print_tree()

    #loops until there is both a found and a not found case
    print("\nfind_node:")
    shown = []
    tries = 0
    while len(shown) < 2:
        value = random.randint(1, 1000)
        tries += 1
        found = tree.find_node(value)
        if found not in shown:
            if found:
                print("find_node(",str(value), "): positive case found on try ",str(tries),sep="")
            else:
                print("find_node(",str(value),"): negative case found on try ",str(tries),sep="")
            shown.append(found)

if __name__ == "__main__":
    main()
