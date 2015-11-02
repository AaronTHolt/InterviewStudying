

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def print_ll(self):
        current = self.head
        while current:
            print current.get_data()
            current = current.get_next()

    def get_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current == None:
            return None
        return current

    def delete(self, data):
        current = self.head
        found = False
        previous = None
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current == None:
            return None
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())



cc = Node()
cc.data = [1,2,3]
ll = LinkedList(cc)
ll.insert(7)
ll.insert([3,4,5])


ll.print_ll()
# print ll.get_size()
print ll.search(7)
# print ll.search(3)
ll.delete(7)
print ll.search(7)
