#link list implementation
from os import link


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
    def addAtPosition(self, value, position):
        current = self.head
        count = 1
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return True
        elif position == False or self.size < position:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
            return True
        else:    
            while count <= position and current is not None:
                print(position, count)
                count += 1
                if position == 1:
                    new_node = Node(value)
                    new_node.next = current
                    self.head = new_node
                    self.size +=1
                    return True
                elif count == position:
                    new_node = Node(value)
                    new_node.next = current.next
                    self.head = new_node
                    self.size += 1
                    return True
                else:
                    curent = current.next
            return False
        

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
    def update(self, value, update):
        current = self.head        
        while current is not None:
            if current.value == value:
                current.value = update
                break
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
print(obj.search(3))
obj.print()
obj.remove(3)
obj.print()
print('updated value')
obj.update(4,7)
obj.print()
input = int(input('enter the value to be added'))
print('add position')
obj.addAtPosition(8,input)
obj.print()

#compare two link list
list1 = LinkList()
list1.add(2)
list1.add(3)
list1.add(4)
list1.add(5)
list1.add(7)

list2 = LinkList()
list2.add(2)
list2.add(3)
list2.add(4)
list2.add(5)
list2.add(7)

def compare(list1, list2):
    if list1.get_size() != list2.get_size():
        return False
    else:
        current1 = list1.head
        current2 = list2.head
        while current1 is not None:
            if current1.value != current2.value:
                return False
            else:
                current1 = current1.next
                current2 = current2.next
        return True
print(compare(list1, list2))


