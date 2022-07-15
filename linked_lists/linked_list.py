from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def set_head(self, head_node):
        self.head = head_node

    def __len__(self):
        cnt = 0

        cur = self.head
        while cur:
            cnt += 1
            cur = cur.get_next()

        return cnt

    def __str__(self):
        cur = self.head
        output = ""

        while cur:
            output += str(cur) + "->"
            cur = cur.get_next()

        return output

    def pop(self):
        if self.head:
            self.head = self.head.get_next()
        else:
            raise IndexError("Unable to pop from empty list")

    def contains(self, value):
        cur = self.head

        while cur:
            if cur.get_data() == value:
                return True
            cur = cur.get_next()

        return False

    def delete(self, value):
        cur = self.head
        prev = cur

        while cur:
            if cur.get_data() == value:
                if prev:
                    prev.set_next(cur.get_next())
                else:
                    self.head = cur.get_next()
                return

            prev = cur
            cur = cur.get_next()

    def push(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.set_head(node)

    def append(self, value):
        node = Node(value)
        cur = self.head

        if not cur:
            self.head = node
            return

        while cur.get_next():
            cur = cur.get_next()

        cur.set_next(node)
