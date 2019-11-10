
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, value, position=0):
        self.insert_node(Node(value), position=position)

    def append(self, value):
        self.append_node(Node(value))

    def remove_duplicates(self):
        values = set()
        node = self.head
        if not node:
            return
        values.add(node.value)

        while node.next:
            if node.next.value in values:
                node.next = node.next.next
            else:
                values.add(node.next.value)
                node = node.next


    def length(self):
        length = 0
        node = self.head
        while node:
            node = node.next
            length += 1
        return length

    # inserts to head
    def insert_node(self, node, position=0):
        if position == 0:
            head = self.head
            self.head = node
            self.head.next = head
        else:
            pass

    def append_node(self, node):
        if not self.head:
            self.head = node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = node

    def print(self):
        print("[", end = '')
        if (self.head):
            current_node = self.head

            while(current_node):
                print('{}'.format(current_node.value), end = '')
                if current_node.next:
                    print(', ', end = '')
                current_node = current_node.next
        print("]")

l = LinkedList()
l.append_node(Node(2))
l.append(3)
l.append_node(Node(4))
l.insert(1)
l.insert(7)
l.print()
print(l.length())
l.remove_duplicates()
l.print()
l.insert(1)
l.append(1)
l.append(3)
l.print()
l.remove_duplicates()
l.print()