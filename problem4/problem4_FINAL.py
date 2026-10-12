class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class SortedDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def node_loc(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("Error: index out of range")
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def unlink(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.size -= 1

    def add(self, value):
        new_node = Node(value)
        self.size += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        temp = self.head
        while temp and temp.value <= value:
            temp = temp.next
        if not temp:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return
        new_node.prev = temp.prev
        new_node.next = temp
        if temp.prev:
            temp.prev.next = new_node
        else:
            self.head = new_node
        temp.prev = new_node

    def delete(self, value):
        temp = self.head
        while temp and temp.value < value:
            temp = temp.next
        if not temp or temp.value != value:
            return False
        self.unlink(temp)
        return True

    def exists_from(self, node, value):
        if not node or node.value > value:
            return False
        if node.value == value:
            return True
        return self.exists_from(node.next, value)

    def exists(self, value):
        return self.exists_from(self.head, value)

    def print_from(self, node):
        if not node.next:
            print(node.value)
            return
        print(node.value, end=" <-> ")
        self.print_from(node.next)

    def print_list(self):
        if not self.head:
            print("(empty)")
            return
        self.print_from(self.head)

    def total_from(self, node):
        if not node:
            return 0
        return node.value + self.total_from(node.next)

    def total(self):
        return self.total_from(self.head)

    def sum_middle_three(self):
        if self.size < 3:
            raise ValueError("sum_middle_three rquires at least 3 nodes")
        mid = self.size // 2
        if self.size % 2 == 1:
            temp = self.node_loc(mid - 1)
        else:
            temp = self.node_loc(mid - 2)
        return temp.value + temp.next.value + temp.next.next.value

    def median(self):
        if self.size == 0:
            raise ValueError("median of an empty list")
        temp = self.node_loc(self.size // 2)
        if self.size % 2 == 1:
            return temp.value
        return (temp.prev.value + temp.value) / 2

    def count_from(self, node, value):
        if not node or node.value > value:
            return 0
        if node.value == value:
            return 1 + self.count_from(node.next, value)
        return self.count_from(node.next, value)

    def count(self, value):
        return self.count_from(self.head, value)
