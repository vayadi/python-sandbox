
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        self.append_node(Node(value))

    def last_node(self):
        node = self.head
        while node.next:
            node = node.next
        return node

    def append_node(self, node):
        if not self.head:
            self.head = node
            return
        last_node = self.last_node()
        node.prev = last_node
        last_node.next = node

    def print(self):
        print("[", end='')
        if self.head:
            current_node = self.head

            while current_node:
                print('{}'.format(current_node.value), end='')
                if current_node.next:
                    print(', ', end='')
                current_node = current_node.next
        print("]")


if __name__ == '__main__':
    print(1)

    l = DoubleLinkedList()
    l.append(3)
    l.append(7)
    l.append(8)
    l.print()
