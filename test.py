class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.head)

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def insertByPosition(self, data, position=False):
        current = self.head
        count = 1
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return True
        elif position == False or self.size < position:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
            return True
        else:    
            while count <= position and current is not None:
                print(position, count)
                count += 1
                if position == 1:
                    new_node = Node(data)
                    new_node.next = current
                    self.head = new_node
                    self.size +=1
                    return True
                elif count == position:
                    new_node = Node(data)
                    new_node.next = current.next
                    self.head = new_node
                    self.size += 1
                    return True
                else:
                    curent = current.next
            return False
    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return str(values)
obj = LinkList()
obj.insertByPosition(1)
obj.insertByPosition(2)
obj.insertByPosition(3)
print(obj)
obj.insertByPosition(5,6)
print(obj)
                