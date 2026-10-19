class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.peek()
        self.items.pop()
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def reverse_from(self, low, high):
        if low >= high:
            return
        self.items[low], self.items[high] = self.items[high], self.items[low]
        self.reverse_from(low + 1, high - 1)

    def reverse(self):
        self.reverse_from(0, len(self.items) - 1)

    def print_stack(self):
        print(", ".join(str(value) for value in self.items))

class SinglyLinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        value = self.peek()
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.head.value

    def is_empty(self):
        return self.size == 0

    def reverse_from(self, prev, node):
        if not node:
            return prev
        next_node = node.next
        node.next = prev
        return self.reverse_from(node, next_node)

    def reverse(self):
        self.head = self.reverse_from(None, self.head)

    def print_stack(self):
        values = []
        temp = self.head
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        print(", ".join(values[::-1]))

class DoublyLinkedStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        self.size += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        value = self.peek()
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.tail.value

    def is_empty(self):
        return self.size == 0

    def reverse_from(self, node):
        if not node:
            return
        next_node = node.next
        node.next = node.prev
        node.prev = next_node
        self.reverse_from(next_node)

    def reverse(self):
        self.reverse_from(self.head)
        self.head, self.tail = self.tail, self.head

    def print_stack(self):
        values = []
        temp = self.head
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        print(", ".join(values))

def show(name, stack):
    for value in range(1, 11):
        stack.push(value)
    print("Stack implemented as " + name)
    print("Before:  ", end="")
    stack.print_stack()
    stack.reverse()
    print("After:   ", end="")
    stack.print_stack()

if __name__ == "__main__":
    show("an array", ArrayStack())
    print()
    show("a singly linked list", SinglyLinkedStack())
    print()
    show("a doubly linked list", DoublyLinkedStack())
