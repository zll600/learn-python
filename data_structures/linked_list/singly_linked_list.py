# https://docs.python.org/3/library/typing.html?highlight=any#typing.Any
# Special type indicating an unconstrained ty
from typing import Any

class Node:
    def __init__(self, data: Any):
        """
        Create and initialize Node class instance.
        >>> Node(20)
        Node(20)
        >>> Node("Hello, world!")
        Node(Hello, world!)
        >>> Node(None)
        Node(None)
        >>> Node(True)
        Node(True)
        """
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        """
        Get the string representation of this node.
        >>> Node(10).__repr__()
        'Node(10)'
        """
        return f"Node({self.data})"

class LinkedList:
    def __init__(self):
        """
        Create and initialize LinkedList class instance.
        >>> linked_list = LinkedList()
        """
        self.head = None

    def __iter__(self) -> Any:
        """
        This function is intended for iterators to access
        and iterate through data inside linked list.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("tail")
        >>> linked_list.insert_tail("tail_1")
        >>> linked_list.insert_tail("tail_2")
        >>> for node in linked_list: # __iter__ used here.
        ...     node
        'tail'
        'tail_1'
        'tail_2'
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        """
        Return length of linked list i.e. number of nodes
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.insert_tail("tail")
        >>> len(linked_list)
        1
        >>> linked_list.insert_head("head")
        >>> len(linked_list)
        2
        >>> _ = linked_list.delete_tail()
        >>> len(linked_list)
        1
        >>> _ = linked_list.delete_head()
        >>> len(linked_list)
        0
        """
        return len(tuple(iter(self)))

    def __repr__(self) -> str:
        """
        String representation/visualization of a Linked Lists
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail(1)
        >>> linked_list.insert_tail(3)
        >>> linked_list.__repr__()
        '1->3'
        """
        # https://docs.python.org/3/library/stdtypes.html?highlight=join#str.join
        return "->".join(str(item) for item in self)

    def __getitem__(self, index: int) -> Any:
        """
        Indexing Support. Used to get a node at particular position
        >>> linked_list = LinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert_nth(i, i)
        >>> all(str(linked_list[i]) == str(i) for i in range(0, 10))
        True
        >>> linked_list[-10]
        Traceback (most recent call last):
        ...
        IndexError: List Index Out Of Range
        >>> linked_list[len(linked_list)]
        Traceback (most recent call last):
        ...
        IndexError: List Index Out Of Range
        """

        if not 0 <= index < len(self):
            raise IndexError("List Index Out Of Range")

        for i, node in enumerate(self):
            if i == index:
                return node
        return None

    def __setitem__(self, index: int, data: Any) -> None:
         """
        >>> linked_list = LinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert_nth(i, i)
        >>> linked_list[0] = 666
        >>> linked_list[0]
        666
        >>> linked_list[5] = -666
        >>> linked_list[5]
        -666
        >>> linked_list[-10] = 666
        Traceback (most recent call last):
        ...
        IndexError: List Index Out Of Range
        >>> linked_list[len(linked_list)] = 666
        Traceback (most recent call last):
        ...
        IndexError: List Index Out Of Range
        """
        if not 0 <= index < len(self):
            raise IndexError("List Index Out Of Range")

        cur = self.head
        for i in range(index):
            cur = cur.next
        cur.data = data

    def insert_tail(self, data: Any) -> None:
        """
        Insert data to the end of linked list.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("tail")
        >>> linked_list
        tail
        >>> linked_list.insert_tail("tail_2")
        >>> linked_list
        tail->tail_2
        >>> linked_list.insert_tail("tail_3")
        >>> linked_list
        tail->tail_2->tail_3
        """
        self.insert_nth(len(self), data)

    def insert_head(self, data: Any) -> None:
        """
        Insert data to the beginning of linked list.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_head("head")
        >>> linked_list
        head
        >>> linked_list.insert_head("head_2")
        >>> linked_list
        head_2->head
        >>> linked_list.insert_head("head_3")
        >>> linked_list
        head_3->head_2->head
        """
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data: Any) -> None:
        """
        Insert data at given index.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first->second->third
        >>> linked_list.insert_nth(1, "fourth")
        >>> linked_list
        first->fourth->second->third
        >>> linked_list.insert_nth(3, "fifth")
        >>> linked_list
        first->fourth->second->fifth->third
        """
        if not 0 <= index < len(self):
            raise IndexError("List Index Out Of Range")

        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next

            new_node.next = tmp.next
            tmp.next = new_node

    def print_list(self) -> None:
        """
        This method prints every node data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first->second->third
        """
        print(self)

    def delete_head(self) -> Any:
        """
        Delete the first node and return the
        node's data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first->second->third
        >>> linked_list.delete_head()
        'first'
        >>> linked_list
        second->third
        >>> linked_list.delete_head()
        'second'
        >>> linked_list
        third
        >>> linked_list.delete_head()
        'third'
        >>> linked_list.delete_head()
        Traceback (most recent call last):
        ...
        IndexError: List index out of range.
        """
        return self.delete_nth(len(self) - 1)

    def delete_tail(self) -> Any:
        """
        Delete the tail end node and return the
        node's data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first->second->third
        >>> linked_list.delete_tail()
        'third'
        >>> linked_list
        first->second
        >>> linked_list.delete_tail()
        'second'
        >>> linked_list
        first
        >>> linked_list.delete_tail()
        'first'
        >>> linked_list.delete_tail()
        Traceback (most recent call last):
        ...
        IndexError: List index out of range.
        """
        return self.delete_tail(0)

    def delete_nth(self, index: int) -> Any:
        """
        Delete node at given index and return the
        node's data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first->second->third
        >>> linked_list.delete_nth(1) # delete middle
        'second'
        >>> linked_list
        first->third
        >>> linked_list.delete_nth(5) # this raises error
        Traceback (most recent call last):
        ...
        IndexError: List index out of range.
        >>> linked_list.delete_nth(-1) # this also raises error
        Traceback (most recent call last):
        ...
        IndexError: List index out of range.
        """
        if not 0 <= index < len(self):
            raise IndexError("List Index Out Of Range")

        delete_node = self.head
        if index == 0:
            self.head = delete_node.next
        else:
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next
            delete_node = tmp.next
            tmp.next = None
        return delete_node.data
    
    def is_empty(self) -> bool:
        """
        Check if linked list is empty.
        >>> linked_list = LinkedList()
        >>> linked_list.is_empty()
        True
        >>> linked_list.insert_head("first")
        >>> linked_list.is_empty()
        False
        """
        return self.head is None

    def reverse(self) -> None:
        """
        This reverses the linked list order.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first->second->third
        >>> linked_list.reverse()
        >>> linked_list
        third->second->first
        """
        prev = None
        cur = self.head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur

            cur = tmp

        self.head = prev

def test_singly_linked_list() -> None:
    """
    >>> test_singly_linked_list()
    """
    linked_list = LinkedList()
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""


if __name__=="__main__":
    import doctest

    doctest.testmod()
