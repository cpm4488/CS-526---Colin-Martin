class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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

    def unlink(self, prev, node):
        if prev:
            prev.next = node.next
        else:
            self.head = node.next
        if node == self.tail:
            self.tail = prev
        self.size -= 1

    def append(self, data):
        new_node = Node(data)
        self.size += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if not self.head:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Error: index out of range")
        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return
        temp = self.node_loc(index - 1)
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        self.size += 1

    def get(self, index):
        temp = self.node_loc(index)
        return temp.data

    def find(self, data):
        temp = self.head
        index = 0
        while temp:
            if temp.data == data:
                return index
            temp = temp.next
            index += 1
        return -1

    def __len__(self):
        return self.size

    def update(self, index, new_val):
        temp = self.node_loc(index)
        temp.data = new_val

    def delete(self, data):
        prev = None
        temp = self.head
        while temp and temp.data != data:
            prev = temp
            temp = temp.next
        if not temp:
            return False
        self.unlink(prev, temp)
        return True

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Error: index out of range")
        prev = None
        if index > 0:
            prev = self.node_loc(index - 1)
        node = prev.next if prev else self.head
        self.unlink(prev, node)
        return node.data

    def print_list(self):
        temp = self.head
        if not temp:
            print("(empty)")
            return
        while temp.next:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data)

    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.print_list()
    sll.append(3)
    sll.append(2)
    sll.update(1, 9)
    sll.append(45)
    sll.prepend(4)
    sll.delete(9)
    sll.append(7)
    sll.prepend(5)
    sll.append(14)
    sll.insert(3, 12)

    print("list:")
    sll.print_list()

    print("get(2):", sll.get(2))
    print("find(45):", sll.find(45))
    print("find(100):", sll.find(100))
    print("length:", len(sll))
    print("delete_at(0):", sll.delete_at(0))

    print("forward:")
    sll.traverse_forward()
