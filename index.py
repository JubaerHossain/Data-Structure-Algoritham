#link list implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkList(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, value):
        current = self.head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return True
            else:
                previous = current
                current = current.next
        return False

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def print(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next

        print(values)

    def get_size(self):
        return self.size



obj = LinkList()
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
obj.print()
obj.remove(3)

obj.print()
