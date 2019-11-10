
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

    def insert_node(self, node, position=0):
        if position == 0:
            head = self.head
            self.head = node
            self.head.next = head
        else:
            idx = 0
            n = self.head
            n_prev = None
            while(n):
                if idx == position:
                    node.next = n
                    n_prev.next = node
                    return
                idx += 1
                n_prev = n
                n = n.next

    def remove_value(self, value):
        node = self.head
        print("""To be implemented""")

    def get_node_with_position(self, position):
        if position < 0:
            return None
        else:
            idx = 0
            node = self.head
            while(node):
                if idx < position:
                    node = node.next
                    idx += 1
                elif idx == position:
                    return node

    def last_node(self):
        node = self.head
        while(node.next):
            node = node.next
        return node

    def append_node(self, node):
        if not self.head:
            self.head = node
            return
        self.last_node().next = node

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
l.insert(137, 2)
l.print()
print(l.get_node_with_position(2).value)
l.insert(3, 3)
l.remove_value(3)
l.print()
l.remove_value(1)
l.print()
